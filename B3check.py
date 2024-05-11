import requests
from bs4 import BeautifulSoup

def find_braintree_sites():
    query = 'Braintree payment site:.com'  # Adjust the search query as needed
    url = f"https://www.google.com/search?q={query}"

    # Set a user-agent to prevent Google from blocking our request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract search results
    search_results = soup.find_all('a')

    # Print URLs of the search results
    for result in search_results:
        url = result.get('href')
        if url.startswith('/url?q='):
            url = url.split('/url?q=')[1].split('&')[0]
            if 'braintree' in url:
                print(url)

if __name__ == "__main__":
    find_braintree_sites()
