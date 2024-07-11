import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/search?q=mobiles+under+50000'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all('div', class_='_1AtVbE')  # Adjust the class based on the structure of the site

    for product in products:
        title = product.find('div', class_='_4rR01T').text.strip()
        price = product.find('div', class_='_30jeq3 _1_WHN1').text.strip()
        rating = product.find('div', class_='_3LWZlK').text.strip()

        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Rating: {rating}")
        print("-" * 20)

else:
    print(f"Failed to retrieve data: {response.status_code}")
