# Bot Discord avec OpenAI et Brave

## Introduction
Ce projet développe un bot Discord qui utilise OpenAI pour traiter les demandes des utilisateurs et Brave pour effectuer des recherches pertinentes. Le projet utilise Docker pour créer un environnement de déploiement uniforme et GitHub Actions pour automatiser le processus de déploiement sur une machine virtuelle Azure.

## Table des Matières
1. [Prérequis](#prérequis)
2. [Configuration des clés API](#configuration-des-clés-api)
3. [Configuration de GitHub et des secrets](#configuration-de-github-et-des-secrets)
4. [Préparation de l'environnement de développement](#préparation-de-lenvironnement-de-développement)
5. [Configuration du Dockerfile](#configuration-du-dockerfile)
6. [Mise en place du CI/CD avec GitHub Actions](#mise-en-place-du-cicd-avec-github-actions)
7. [Déploiement sur la VM Azure](#déploiement-sur-la-vm-azure)
8. [Démarrage et tests](#démarrage-et-tests)
9. [Améliorations futures](#améliorations-futures)

## Prérequis
- Python 3.8 ou plus récent.
- Compte GitHub.
- Compte Azure avec une VM configurée.
- Accès administrateur sur un serveur Discord.

## Configuration des clés API
Pour que le bot fonctionne correctement, vous aurez besoin de clés API pour Discord, OpenAI, et Brave.

### Clé API Brave
1. Visitez [Brave API](https://api.search.brave.com/) et suivez les instructions pour obtenir une clé API.

### Token OpenAI
1. Créez un compte sur [OpenAI](https://platform.openai.com/signup).
2. Accédez à la gestion des API et créez un token pour votre application.

### Clé BOT Discord
1. Allez sur le [portail des développeurs Discord](https://discord.com/developers/applications).
2. Créez une nouvelle application et sous l'onglet "Bot", créez un nouveau bot.
3. Copiez le token du bot.

## Configuration de GitHub et des secrets
Pour sécuriser les clés API et permettre le déploiement automatique, nous utiliserons les secrets de GitHub.

### Déclaration des secrets
1. Dans votre dépôt GitHub, naviguez à "Settings" > "Secrets" > "Actions".
2. Ajoutez les secrets suivants :
   - `BRAVE_KEY`: Votre clé API Brave.
   - `OPENAI_API_TOKEN`: Votre token OpenAI.
   - `DISCORD_KEY`: Votre clé bot Discord.
   - `SSH_PRIVATE_KEY`: La clé privée SSH que vous utiliserez pour l'accès à votre VM Azure.

### Création d'une paire de clés SSH
1. Sur votre terminal local, exécutez :
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ````
2. Lorsque vous êtes invité à saisir un fichier pour enregistrer la clé, vous pouvez appuyer sur Entrée pour utiliser l'emplacement par défaut.
3. Ajoutez la clé publique (`id_rsa.pub`) à votre VM Azure sous `~/.ssh/authorized_akeys`.

## Préparation de l'environnement de développement
1. Clonez votre dépôt GitHub sur votre machine locale.
2. Créez un environnement virtuel Python et activez-le :
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Unix
   .\.venv\Scripts\Activate.ps1  # Windows
   ````
3. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ````

## Configuration du Dockerfile
Créez un `Dockerfile` à la racine de votre projet avec le contenu suivant pour définir l'environnement de votre application :
   ```dockerfile
   # Utiliser une image de base Python
   FROM python:3.10-slim

   # Définir le répertoire de travail dans le conteneur
   WORKDIR /app

   # Copier les fichiers du dossier local au dossier de travail dans le conteneur
   COPY . /app

   # Installer les dépendances Python spécifiées dans requirements.txt
   RUN pip install --no-cache-dir -r requirements.txt

   # Exposer un port, si votre bot utilise des fonctionnalités qui requièrent un port externe (optionnel)
   EXPOSE 5000

   # Commande pour démarrer l'application
   CMD ["python", "bot.py"]
   ````

## Mise en place du CI/CD avec GitHub Actions
Créez un fichier `.github/workflows/ci-cd.yml` dans votre dépôt avec le contenu suivant pour automatiser le déploiement :
   ```yaml
   name: CI/CD Pipeline

   on:
     push:
       branches:
         - main

   jobs:
     build_and_deploy:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2

         - name: Set up SSH key
           uses: webfactory/ssh-agent@v0.5.3
           with:
             ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}

         - name: Set up Docker
           uses: docker/setup-buildx-action@v1

         - name: Build and Push Docker image
           uses: docker/build-push-action@v2
           with:
             context: .
             file: ./Dockerfile
             tags: yourusername/yourrepo:latest
             push: true

         - name: Deploy to Azure VM
           run: ssh username@vm-ip-address 'docker pull yourusername/yourrepo:latest && docker run ...'
   ````

## Déploiement sur la VM Azure
Assurez-vous que Docker est installé sur votre VM Azure et que vous pouvez y accéder via SSH. Le workflow CI/CD s'occupera de construire l'image Docker et de la déployer chaque fois que vous pousserez sur la branche principale.

## Démarrage et tests
Pour tester localement, exécutez :
   ```bash
   python bot.py
   ````
Pour voir votre bot en action, invitez-le sur un serveur Discord et interagissez avec lui.

## Améliorations futures
- Ajout de fonctionnalités de personnalisation pour les réponses du bot.
- Amélioration du scraping des données pour les recherches avec Brave.
- Intégration de la reconnaissance visuelle pour analyser les images et répondre en conséquence.
