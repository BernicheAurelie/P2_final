import shutil
import requests
import scraping
from pathlib import Path

DATA_DIR = Path(".")/"Data"
def get_image(book):
    path = DATA_DIR/book["category"]/"image"
    path.mkdir(parents=True, exist_ok=True)
    filename = book['upc'] + '.jpg'
    filePath = path/filename
    r = requests.get(book['url_image'], stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with filePath.open('wb') as f: 
            shutil.copyfileobj(r.raw, f)
