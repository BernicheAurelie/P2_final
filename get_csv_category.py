import dictwriter_csv
from bs4 import BeautifulSoup
import utils
import scraping
import get_product_url_for_category

def get_csv_category(links):
    for link in links:
        # soup = utils.request(link)#r = requests.get(link)
        book = scraping.scrap_book(link)
        dictwriter_csv.write_csv(book)

#category_url='http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html'
#links = get_product_url_for_category.get_product_url_for_category(category_url)
#file = get_csv_category(links)