# BeautifulSoup (bs4) is a Python library used for web scraping — it helps extract data from HTML and XML files.

from bs4 import BeautifulSoup
import requests

url = "https://google.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)  # Get page title