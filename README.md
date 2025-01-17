# Nom du projet

APPLICATION WEB POUR AIDER LES ASSOCIATIONS ENGAGEES DANS L'AIDE CARITATIVE

## Table des Matieres

- [Introduction](#introduction)
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribution](#contribution)
- [Licence](#licence)
- [Contact](#contact)

## Introduction

Cette application web est conçue pour aider les associations caritatives à gérer leurs opérations quotidiennes, à suivre les bénévoles,

les dons et les évènements. Le projet utilise le Framework Django pour une infrastructure robuste et évolutive.

## Fonctionnalités

- Authentification et autorisation
- Gestion des bénévoles et des membres de l'association
- Suivi des dons
- Organisation et plannification des évènements
- Tableau de bord pour l'administration

## Prérequis

Avant d'installer et d'utiliser l'application, assurez vous d'avoir les éléments suivants :

- python 3.12.2
- Django 5.0.4
- SQLite, PostgreSQL ou tout autre SGBD compatible avec Django
- Git

## Installation

Suivez ces etapes pour installer et configurer le projet localement :

1.  Clonez le depot :
    ''' sh

        git clone https://github.com/StephaneGradX/SolidAid.git
        cd SolidAid

'''

2.  Creez et activez un environnement virtuel :
    ''' sh

        python -m venv env
        source env\Scripts\activate           #sur Windows

    '''

3.  Installez les dependances :
    ''' sh

        pip install -r requirements.txt

    '''

4.  Configurez la base de données dans "settings.py" :
    ''' python

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'votre_db',
                'USER': 'votre_utilisateur',
                'PASSWORD': 'votre_mot_de_passe',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }

'''

5.  Appliquez les migrations :
    ''' sh

        python manage.py migrate

    '''

6.  Creez un super-utilisateur pour accéder à la page admin :
    ''' sh

        python manage.py createsuperuser

    '''

7.  Lancez le serveur de developpement :
    ''' sh

        python manage.py runserver

    '''

## Utilisation

Accédez à l'application via 'https://localhost:8000'. Connectez vous à l'interface d'administration via 'https://localhost:8000/admin'

avec les identifiants du super-utilisateur que vous avez créés.

## Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le depot
2. Creez une branche de fonctionnalites ('git checkout -b feature/AmazingFeature')
3. Commitez vos modifications ("git commit -m 'Add some Feature' ")
4. Poussez vers la branche ('git push origin feature/AmazingFeature')
5. Ouvrez une Pull Request

## Licence

Distribué sous la licence MIT. Voir 'LICENCE' pour plus d'informations

## Contact

NKE OLINGA STEPHANE JOEL - [joeldragnir490@gmail.com](mailto:joeldragnir490@gmail.com)

Lien du projet : [https://github.com/StephaneGradX/SolidAid](https://github.com/StephaneGradX/SolidAid)
