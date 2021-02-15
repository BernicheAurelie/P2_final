import requests
from bs4 import BeautifulSoup 


def request(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content,"lxml")
	return soup

def get_content(url):
	img = requests.get(url).content
	return img
