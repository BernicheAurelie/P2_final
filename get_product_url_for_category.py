"""utils module give us HTML code to parse informations inside it
"""
import utils

def get_article(articles):
    """from article tags get ahref to create a list of books url"""
    links = list()
    for article in articles:
        a = article.find('a')
        link = a['href']
        url_article = link.replace('../../../', 'http://books.toscrape.com/catalogue/')
        links.append(url_article)
    return links

def get_product_url_for_category(category_url):
    """for each category we get books url inside it
    still next page is disponible
    """
    links = list()
    soup = utils.request(category_url)
    bouton_next = soup.find("li", {"class": "next"})
    index = 1
    articles = soup.find_all('article', 'product_pod')
    category_base = category_url
    links.extend(get_article(articles))
    while bouton_next is not None:
        index +=1
        category_url = category_base.replace("index.html", "page-" + str(index) + '.html')
        soup = utils.request(category_url)
        articles = soup.find_all('article', 'product_pod')
        bouton_next = soup.find("li", {"class": "next"})
        links.extend(get_article(articles))
    return links
