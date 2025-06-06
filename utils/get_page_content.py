import requests
from bs4 import BeautifulSoup
from utils.get_random_headers import get_random_header

def get_page_content(url):
    response = requests.get(url, headers=get_random_header())
    soup = BeautifulSoup(response.content, "html.parser")
    return soup