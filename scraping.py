"""utils module give us HTML code to parse informations inside it
"""
import utils


def get_upc(soup):
    """find upc searching text inside td tags"""
    upc = soup.find('td').text
    return upc

def get_title(soup):
    """find product title inside high title tags"""
    title = soup.find('h1').text
    return title

def get_product (soup):
    """get product page url inside article tags"""
    product = soup.find("article", "product_page")
    return product

def get_url_image (soup):
    """get image url inside src attribute and concatenate it"""
    product = soup.find("article", "product_page")
    image = product.img["src"] .replace("../..", "http://books.toscrape.com")
    return image

def get_review_rating (soup):
    """find rating inside class attribute from p tags"""
    product = soup.find("article", "product_page")
    review_rating = product.find("p", "star-rating")["class"][-1]
    return review_rating

def get_category (soup):
    """get category product inside ul then a tags"""
    category = soup.find('ul').find_all('a')[2].text
    return category

def get_number_available (soup):
    """find product disponibility in class attribute from p tags"""
    number_available = soup.find('p', {'class':'instock availability'}).text.strip()
    return number_available

def get_price_excl_tax (soup):
    """find price excluding taxes from list of td tags"""
    tds = soup.find_all('td')
    liste = []
    for td in tds:
        liste.append(td.text)
    price_excl_tax = liste[2]
    return price_excl_tax

def get_price_incl_tax (soup):
    """find price including taxes from list of td tags"""
    tds = soup.find_all('td')
    liste = []
    for td in tds:
        liste.append(td.text)
    price_incl_tax = liste[3]
    return price_incl_tax

def get_product_description (soup):
    """get the pitch book in list of p tags"""
    ps = soup.find_all ('p')
    liste_p = []
    for p in ps:
        liste_p.append(p.text)
    product_description = liste_p[3]
    return product_description

def scrap_book(url):
    """get all the informations from a product url into a dictionnary"""
    book = dict()
    soup = utils.request(url)
    book["product_page_url"] = url
    book["title"] = get_title(soup)
    book["url_image"] = get_url_image(soup)
    book["category"] = get_category(soup)
    book["upc"] = get_upc(soup)
    book["review_rating"] = get_review_rating(soup)
    book["number_available"] = get_number_available(soup)
    book["price_excl_tax"] = get_price_excl_tax(soup)
    book["price_incl_tax"] = get_price_incl_tax(soup)
    book["product_description"] = get_product_description (soup)
    return book
