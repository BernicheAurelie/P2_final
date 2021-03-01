# P2_final


[![Generic badge](https://img.shields.io/badge/MADE_WITH-PYTHON-blueviolet.svg)](https://shields.io/)   
[![Generic badge](https://img.shields.io/badge/APPROVED_BY-AURELIE_BERNICHE-blueviolet.svg)](https://shields.io/)


Ce programme permet de scraper les différents articles du site **Books to Scrape** afin d'en extraire plusieurs informations au moment de son exécution.

## Pour commencer

Ce code est dévéloppé en langage Python. Il a pour but initial d'automatiser la comparaison des prix de livres d'occasion sur différents sites de ventes en ligne.  
Ce programme va vous permettre de récupérer des informations par catégorie d'ouvrage et également de télécharger les différentes images des livres.

### Pré-requis

- Python 3  [Download Python](https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe)  
- Visual Studio Code  [Download VS Code](https://code.visualstudio.com/)  
- Dépôt GitHub  [Create a new repository](https://github.com/new)

### Installation

Dans un premier temps, vous devez créer un dossier pour ce programme afin de télécharger l'application:  
1) ```mkdir projet2```: Créer un dossier projet2 
2) ```cd projet2```: Se placer dans ce dossier
3) ```git clone https://github.com/BernicheAurelie/P2_final.git```: Cloner le repository contenant l'application  
4) ```cd P2_final```: Se placer dans le dépôt cloné
5) ```Python -m venv env```  : Créer l'environnement virtuel
6) Cet environnement nécessite d'être activé via:  
sous Windows: ```source env/scripts/activate```  
sous Mac/Linux: ```source env/bin/activate```  
7)```pip install -r requirements.txt```: Récupérer les modules nécessaires à l'application du code, contenus dans le fichier **requirements.txt**.  

## Démarrage

Vous pouvez maintenant lancer l'application avec la commande suivante:  
```python main.py```  
Celle-ci va alors vous permettre de récupérer les données selectionnées du site.  
Un dossier **Data** va être créer ainsi qu'à l'intérieur, un sous-dossier par catégorie.   
Celui-ci contiendra d'une part un fichier **csv** avec les données de tous les livres  
et un autre dossier **image** contenant les images téléchargées des différents livres.  

## Fabriqué avec

- [Python 3](https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe) - langage de programmation
- [Visual Studio Code](https://code.visualstudio.com/) - Editeur de textes

## Contributing

**Ranga Gonnage** _[Mentor OpenClassrooms](https://openclassrooms.com/fr/)_

## Versions

**Dernière version :** 1.0

## Auteurs

**Aurélie Berniche** _[lien GitHub](https://github.com/BernicheAurelie)_
