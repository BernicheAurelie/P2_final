"""csv module is using to write file.csv from a dictionnary and pathlib will
permit to define path and check size before creating it
"""
import csv
from pathlib import Path


DATA_DIR = Path(".")/"Data"
"""create a constante to select the path to execute the function"""

def write_csv(book):
    """create a new directory if it doesn't exist with the variable name
    defined with a key from our dictionnary
    from dictionnary write a csv file
    with keys in fieldnames and values in followings rows
    """
    path = DATA_DIR/book["category"]
    path.mkdir(parents=True, exist_ok=True)
    file_path = path/"product.csv"
    with file_path.open(mode='a+', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=book.keys(),delimiter=",", lineterminator = "\n")
        if file_path.stat().st_size == 0:
            writer.writeheader()
        writer.writerow(book)
