import pandas as pd
import requests
from bs4 import BeautifulSoup

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept': 'application/json',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
# }

url="https://www.flipkart.com/"
r=requests.get(url)
print(r)

# soup=BeautifulSoup.find_all(r.text,"lxml")
# print(soup)