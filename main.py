"""def_get_categories module to get book categories in the website
get_product_url_for_category is using to get our book url
and get_csv_category will permit us to write our dictionnaries in file
and download the corresponding pictures.
tqdm is using to show us the progression during code execution.
"""
from tqdm import tqdm
import def_get_categories
import get_product_url_for_category
import get_csv_category

if __name__ == "__main__":
    BOOKS_TO_SCRAP = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    categories_url = def_get_categories.get_categories(BOOKS_TO_SCRAP)
    for category_url in tqdm(categories_url):
        links = get_product_url_for_category.get_product_url_for_category(category_url)
        get_csv_category.get_csv_category(links)
        get_csv_category.download_images(links)
