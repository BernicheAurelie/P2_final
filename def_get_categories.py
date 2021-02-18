"""utils module give us HTML code to parse informations inside it
"""
import utils

def get_categories (bookstoscrap):
    """get a list of book categories from website searching in <a> tags"""
    soup = utils.request(bookstoscrap)
    cat = soup.find_all("a")
    links_category = []
    for link in cat:
        category = link.get("href")
        cat_url = category.replace("../books", "http://books.toscrape.com/catalogue/category/books")
        links_category.append(cat_url)
    categories_url = links_category[3:53]
    return categories_url
    