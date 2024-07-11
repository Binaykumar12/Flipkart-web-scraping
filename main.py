import requests
import time
import random
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/some-product-page'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

for _ in range(10):  # Example loop for multiple requests
    response = requests.get(url, headers=headers)
    print("Response status code:", response.status_code)

    if response.status_code == 200:
        print("Success!")
        soup = BeautifulSoup(response.content, 'html.parser')
        # Process the content with BeautifulSoup here
        # Example: Extract the title of the page
        title = soup.title.string
        print("Page Title:", title)
    elif response.status_code == 429:
        retry_after = int(response.headers.get('Retry-After', 60))  # Default to 60 seconds if not specified
        print(f"Rate limited. Retrying after {retry_after} seconds.")
        time.sleep(retry_after)
    else:
        print("Failed to retrieve the page.")

    time.sleep(random.uniform(1, 3))  # Sleep for a random time between 1 and 3 seconds
