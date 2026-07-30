# Import requests to download the webpage
import requests

# Import BeautifulSoup to parse HTML
from bs4 import BeautifulSoup

# Website we want to scrape
url = "https://quotes.toscrape.com"

# Send a GET request to the website
response = requests.get(url)

# Convert the HTML into a BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Find the first quote on the page
first_quote = soup.find("span", class_="text")

# Print only the text inside the HTML tag
print(first_quote.text) 