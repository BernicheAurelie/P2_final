"""scraping module to scrap website and get a dictionnary
dictwriter_csv module to write our datas in file
and get_image module is using to download images
"""
import scraping
import dictwriter_csv
import get_image

def get_csv_category(links):
    """final function to write csv file with scraping items from the categories list"""
    for link in links:
        book = scraping.scrap_book(link)
        dictwriter_csv.write_csv(book)

def download_images(links):
    """download images from the url image get in our dictionnary from the categories list"""
    for link in links:
        book = scraping.scrap_book(link)
        get_image.get_image(book)
