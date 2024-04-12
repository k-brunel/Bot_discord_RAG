# Création d'un bot Discord interfacé avec OpenAI et Brave

Ce projet consiste en un bot Discord qui utilise OpenAI pour traiter les demandes des utilisateurs et Brave pour rechercher des informations pertinentes, permettant une interaction riche et intelligente.

## Configuration initiale

### Création et invitation du BOT Discord
Pour créer et inviter le bot Discord sur un serveur où vous avez des droits ADMIN, suivez les instructions détaillées sur la [documentation officielle de Discord.py](https://discordpy.readthedocs.io/en/latest/discord.html).

### Configuration des clés API
- **Clé API Brave** : Créez une clé API sur [Brave API](https://api.search.brave.com/).
- **Client API pour les requêtes HTTP** : Utilisez [Bruno](https://www.usebruno.com/) pour visualiser les réponses des requêtes.

### Initialisation de l'environnement virtuel
```bash
py -m venv .venv        
.\.venv\Scripts\activate

### Installation des dépendances
pip install -r requirements.txt

### Configuration des variables d'environnement
Créez un fichier .env à la racine du projet et ajoutez vos clés :
brave_key = 'Votre_clé_Brave'
OPENAI_API_TOKEN= 'Votre_token_OpenAI'
discord_key = 'Votre_clé_Discord'

## Démarrage du bot
Pour démarrer le bot, exécutez :
python bot.py

## Améliorations futures
### Personnalisation du bot :
Ajouter la possibilité de configurer la personnalité du bot dans les prompts envoyés à OpenAI pour qu'il réponde avec des nuances spécifiques, comme une touche d'humour.

### Amélioration de la récupération des données :
Enrichir les données extraites de Brave en implémentant un scraping plus avancé des résultats de recherche.

###Reconnaissance de fichiers :
Intégrer une fonctionnalité de reconnaissance visuelle en utilisant GPT-4 pour permettre au bot d'analyser et de répondre à des images ou d'autres types de fichiers multimédias.
