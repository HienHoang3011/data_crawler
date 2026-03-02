import requests
from bs4 import BeautifulSoup
import re

def get_links_from_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.find("div", class_ = "box")
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        links.append(href)
    with open("links.txt", "w", encoding="utf-8") as f:
        for link in links:
            f.write("https://loigiaihay.com"+link + "\n")
    return links

if __name__ == "__main__":
    url = "https://loigiaihay.com/de-thi-de-kiem-tra-toan-lop-12-c1015.html"  
    get_links_from_page(url)