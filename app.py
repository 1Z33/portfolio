from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
# configuration base SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev_key_a_changer_en_production'

db = SQLAlchemy(app)


# TABLE PROJET
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(200), default='')
    github_link = db.Column(db.String(300), default='')
    image_url = db.Column(db.String(500), default='')


# TABLE CONTACT
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))


# PAGE ACCUEIL
@app.route('/')
def home():
    return render_template('index.html')


# AFFICHER PROJETS
@app.route('/projects')
def projects():
    projects = db.session.execute(db.select(Project)).scalars().all()
    return render_template('projects.html', projects=projects)


# AJOUT PROJET
@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        technologies = request.form.get('technologies', '')
        github_link = request.form.get('github_link', '')
        image_url = request.form.get('image_url', '')
        
        if not title or not description:
            flash("Veuillez remplir tous les champs obligatoires.", "error")
            return render_template('add_projet.html')

        new_project = Project(
            title=title,
            description=description,
            technologies=technologies,
            github_link=github_link,
            image_url=image_url
        )

        db.session.add(new_project)
        db.session.commit()

        flash("Projet ajouté avec succès !", "success")
        return redirect(url_for('projects'))

    return render_template('add_projet.html')


# MODIFIER PROJET
@app.route('/edit_project/<int:id>', methods=['GET', 'POST'])
def edit_project(id):
    project = db.get_or_404(Project, id)

    if request.method == 'POST':
        project.title = request.form['title']
        project.description = request.form['description']
        project.technologies = request.form.get('technologies', '')
        project.github_link = request.form.get('github_link', '')
        project.image_url = request.form.get('image_url', '')

        db.session.commit()
        flash("Projet mis à jour !", "success")

        return redirect(url_for('projects'))

    return render_template('edit_project.html', project=project)


# SUPPRIMER PROJET
@app.route('/delete_project/<int:id>')
def delete_project(id):
    project = db.get_or_404(Project, id)

    db.session.delete(project)
    db.session.commit()

    flash("Projet supprimé.", "info")
    return redirect(url_for('projects'))


# CONTACT
@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not message:
            flash("Veuillez remplir tous les champs du formulaire de contact.", "error")
            return render_template('contact.html')

        new_message = Contact(
            name=name,
            email=email,
            message=message
        )

        db.session.add(new_message)
        db.session.commit()

        flash("Votre message a été envoyé avec succès !", "success")
        return redirect(url_for('home'))

    return render_template('contact.html')


# AFFICHER MESSAGES
@app.route('/messages')
def messages():
    messages = db.session.execute(db.select(Contact)).scalars().all()
    return render_template('messages.html', messages=messages)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)