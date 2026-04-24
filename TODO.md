# TODO - Mise à jour Portfolio Flask

## Plan d'implémentation

### 1. app.py - Modèles et routes
- [x] Corriger render_template('add_project.html') → 'add_projet.html'
- [x] Ajouter `technologies`, `github_link`, `image_url` au modèle Project
- [x] Ajouter `created_at` au modèle Contact
- [x] Mettre à jour route add_project avec nouveaux champs
- [x] Mettre à jour route edit_project avec nouveaux champs

### 2. Templates
- [x] contact.html - Supprimer WhatsApp, remettre vrai formulaire Flask POST
- [x] add_projet.html - Ajouter champs technologies, github, image
- [x] edit_project.html - Ajouter champs technologies, github, image (pré-remplis)
- [x] projects.html - Afficher technologies (badges), GitHub link, image
- [x] messages.html - Afficher date/heure du message

### 3. CSS
- [x] Ajouter styles pour badges tech, lien GitHub, image projet

### 4. Base de données
- [x] Supprimer portfolio.db obsolète pour recréation auto

### 5. Test
- [x] Lancer app et vérifier toutes les fonctionnalités — Serveur actif sur http://127.0.0.1:5000

