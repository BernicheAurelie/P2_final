import csv
from pathlib import Path
DATA_DIR = Path(".")/"Data" #on crée une variable fixe pour etre dans le dossier parent
def write_csv(book): #book peut s'appeler toto mais toto doit être un dict
    path = DATA_DIR/book["category"] #le chemin va etre notre dossier parents DATA_DIR
                        # plus la valeur associée à notre clé qui est une variable
    path.mkdir(parents=True, exist_ok=True) # si le dossier n'existe pas on le crée 
    filePath = path/"product.csv" # on crée notre fichier "file.csv"
    with filePath.open(mode='a+', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=book.keys(),delimiter=",", lineterminator = "\n")
        if filePath.stat().st_size == 0:  #si sa taille est nulle on ecrit les fieldnames
             writer.writeheader() 
        writer.writerow(book) # sinon on ecrit les lignes



