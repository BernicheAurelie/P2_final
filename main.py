
import get_product_url_for_category
import get_csv_category
import def_get_categories
import dictwriter_csv
import dictwriter3_csv
import requests
import scraping
import reader


if __name__ == "__main__":
    bookstoscrap = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    categories_url = def_get_categories.get_categories(bookstoscrap)
    for category_url in categories_url:
        links = get_product_url_for_category.get_product_url_for_category(category_url)
        get_csv_category.get_csv_category(links)
        get_csv_category.download_images(links)
