import dictwriter_csv
import scraping
import get_image


def get_csv_category(links):
    for link in links:
        book = scraping.scrap_book(link)
        dictwriter_csv.write_csv(book)
        
def download_images(links):
    for link in links:
        book = scraping.scrap_book(link)
        get_image.get_image(book)
