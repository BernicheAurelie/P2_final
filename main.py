
import get_product_url_for_category
import get_csv_category

if __name__ == "__main__":
    category_url = 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html'
    links = get_product_url_for_category.get_product_url_for_category(category_url)
    get_csv_category.get_csv_category(links)
