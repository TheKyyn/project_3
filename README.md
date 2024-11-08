# Big Data Application Project - Hétic 2024 - WEB2

## Description

Ce projet est une application Big Data backend développée avec Python et Flask, accompagnée d'un frontend minimaliste en JavaScript Vanilla. Le but est de traiter et de gérer des données volumineuses en utilisant une base de données PostgreSQL optimisée pour le Big Data. L'infrastructure inclut Docker, Prometheus pour la surveillance, et Grafana pour la visualisation des métriques.

## Table des Matières

1. [Prérequis](#prérequis)
2. [Installation et Configuration](#installation-et-configuration)
3. [Utilisation](#utilisation)
4. [Structure du Projet](#structure-du-projet)
5. [Tests](#tests)
6. [Surveillance et Monitoring](#surveillance-et-monitoring)
7. [Endpoints API](#endpoints-api)

## Prérequis

- **Docker** et **Docker Compose** installés sur votre machine.
- **Python 3.9** (pour exécuter et tester localement sans Docker).
- **Git** pour cloner le dépôt.

## Installation et Configuration

### Cloner le dépôt

```bash
git clone https://github.com/TheKyyn/project_3.git
cd project_3
```

### Configurer la base de données

Assurez-vous que Docker est démarré, puis exécutez :

```bash
docker-compose up --build
```

Cela téléchargera les images nécessaires et démarrera les services de base de données, backend, Prometheus, et Grafana.

### Initialiser la Base de Données

Après le démarrage, connectez-vous au service de base de données pour créer la table principale `data_records` :

```bash
docker-compose exec db psql -U postgres -d DB_Project_3
```

Dans le shell PostgreSQL, exécutez :

```sql
CREATE TABLE data_records (
    id SERIAL PRIMARY KEY,
    data_value TEXT NOT NULL,
    category TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL
);
```

Vous pouvez quitter PostgreSQL avec `\q`.

## Utilisation

### Accéder à l'Interface Utilisateur

L'application frontend est accessible via `index.html` à la racine du projet. Ouvrez ce fichier dans un navigateur. Pour interagir avec les données, vous pouvez :

- **Effectuer des recherches** : Saisissez une catégorie dans le champ et cliquez sur "Rechercher".
- **Ajouter des données** : Utilisez le formulaire pour ajouter des données à la base.

### Accéder à l'API

Vous pouvez interagir avec l'API via les endpoints suivants :

- **Récupérer les données** : `GET http://localhost:5001/data?category=example`
- **Ajouter des données** : `POST http://localhost:5001/data` avec le corps JSON `{ "data_value": "Test Value", "category": "Test Category" }`
- **Voir les statistiques par catégorie** : `GET http://localhost:5001/stats`
- **Surveillance des métriques** : `GET http://localhost:5001/metrics`

## Structure du Projet

```
project_3/
├── app.py                # Fichier principal de l'application Flask
├── Dockerfile            # Dockerfile pour créer l'image du backend Flask
├── docker-compose.yml    # Fichier Docker Compose pour orchestrer les services
├── index.html            # Interface utilisateur de base en HTML/JavaScript
├── requirements.txt      # Dépendances Python
├── setup_db.sql          # Script SQL pour initialiser les tables
├── prometheus.yml        # Configuration de Prometheus
├── locustfile.py         # Scénario de test de charge pour Locust
└── test_app.py           # Tests unitaires pour l'API
```

## Tests

Pour exécuter les tests unitaires, assurez-vous d'être dans un environnement où les dépendances Python sont installées, puis exécutez :

```bash
python -m unittest test_app.py
```

Cela va vérifier la fonctionnalité des principaux endpoints.

## Surveillance et Monitoring

Prometheus et Grafana sont inclus pour la surveillance des métriques de l'application :

- **Prometheus** : accessible via http://localhost:9090
- **Grafana** : accessible via http://localhost:3000
  - Les identifiants par défaut sont `admin` / `admin`.

Prometheus collecte les métriques de l'application Flask, visibles via l'URL `/metrics`.

## Endpoints API

### `GET /data`

- **Description** : Récupère les données, avec une option de filtrage par catégorie.
- **Paramètres de requête** :
  - `category` (optionnel) : Filtre par catégorie.

### `POST /data`

- **Description** : Ajoute une nouvelle entrée de données.
- **Corps JSON** :
  - `data_value` : La valeur des données à stocker.
  - `category` : La catégorie des données.

### `GET /stats`

- **Description** : Récupère les statistiques des données en comptant les occurrences par catégorie.

### `GET /metrics`

- **Description** : Expose les métriques de l'application pour Prometheus.

---

Pour toute question ou clarification, veuillez consulter le dépôt GitHub ou contacter le développeur.

**Lien vers le dépôt** : [https://github.com/TheKyyn/project_3](https://github.com/TheKyyn/project_3)
