"""using module requests and BeautifulSoup to get HTML content from url
"""
import requests
from bs4 import BeautifulSoup


def request(url):
    """get soup product from url to parse it next"""
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    return soup

def get_content(url):
    """get content from url images to download it next"""
    img=requests.get(url).content
    return img
