from bs4 import BeautifulSoup
import utils
import scraping
import csv
import os.path
import dictwriter_csv


def get_article(articles):
    links = list()
    for article in articles:
        a = article.find('a')
        link = a['href']
        url_article = link.replace('../../../', 'http://books.toscrape.com/catalogue/')
        links.append(url_article)
    return links

def get_product_url_for_category(category_url):
    links = list()
    soup = utils.request(category_url)
    boutonNext = soup.find("li", {"class": "next"})
    index = 1
    articles = soup.find_all('article', 'product_pod') 
    category_base = category_url            
    links.extend(get_article(articles))
    
    while boutonNext is not None:
        index +=1
        category_url = category_base.replace("index.html", "page-" + str(index) + '.html')
        soup = utils.request(category_url)# r = requests.get(url)
        articles = soup.find_all('article', 'product_pod')             
        boutonNext = soup.find("li", {"class": "next"})
        links.extend(get_article(articles))
    return links

#category_url='http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
#links = get_product_url_for_category(category_url)
#print(links)
#file = dictwriter_csv.write_csv(links)
