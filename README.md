# P2_final

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)  (https://img.shields.io/static/v1?label=APPROUVED BY&message=AURELIE BERNICHE&color=<BLUEVIOLET>)

Ce programme permet de scraper les différents articles du site **Books to Scrape** afin d'en extraire plusieurs informations au moment de son exécution.

## Pour commencer

Ce code est dévéloppé en langage Python. Il a pour but initial d'automatiser la comparaison des prix de livres d'occasion sur différents sites de ventes en ligne. Ce programme va vous permettre de récupérer des informations par catégorie d'ouvrage et également de télécharger les différentes images des livres.

### Pré-requis

- Python 3
- Visual Studio Code
- Repository GitHub

### Installation

Dans un premier temps, vous devez créer un dossier pour ce programme:
Exécutez la commande ''mkdir projet2'' dans le terminal.
Une fois dans ce nouveau dossier, il faut executer la commande:
''git init projet2'' pour créé un dépôt local.
Vous devez ensuite récupérer le repository GitHub
Pour se faire, exécutez ''git clone https://github.com/BernicheAurelie/P2_final.git ''
Vous devez également créer l'environnement virtuel pour ce projet en exécutant la commande suivante:
''Python -m venv env''
Cet environnement necessite d'être activé via:
sous Windows: ''source env/scripts/activate''
sous Mac/Linux: source env/bin/activate
Avec la commande ''pip install -r'', vous pourrez récupérer les modules nécessaires à l'application du code, contenus dans le fichier **requirements.txt**.

## Démarrage

Ouvrez le dossier précedemment créé **projet2**
puis le fichier **main.py**
exécutez alors le programme dans **main.py**
Celui-ci va alors vous permettre de récupérer les données selectionnées du site.
Un dossier **Data** va être créer ainsi qu'à l'intérieur, un sous-dossier par catégorie. 
Celui-ci contiendra d'une part un fichier **csv** avec les données de tous les livres et un autre dossier **image** contenant les images téléchargées des différents livres.

## Fabriqué avec

* Python 3 https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe - langage de programmation
* Visual Studio Code https://code.visualstudio.com/ - Editeur de textes

## Contributing

Aurélie Berniche

## Versions

**Dernière version :** 1.0

## Auteurs

* **Aurélie Berniche** https://github.com/BernicheAurelie

## License



