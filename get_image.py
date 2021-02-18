"""requests module is using to get url
pathlib will help us to define path
shutil is using to copy object in file
"""
import shutil
from pathlib import Path
import requests


DATA_DIR = Path(".")/"Data"
"""create a constante to select the path to execute the function"""

def get_image(book):
    """Create a new directory, if it doesn't exist, with the variable name
    defined with the category key from our dictionnary.
    From url image on dictionnary get content and write it in binary mode
    in a new file, names with key upc from our dictionnary.
    """
    path = DATA_DIR/book["category"]/"image"
    path.mkdir(parents=True, exist_ok=True)
    filename = book['upc'] + '.jpg'
    file_path = path/filename
    r = requests.get(book['url_image'], stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with file_path.open('wb') as f:
            shutil.copyfileobj(r.raw, f)
