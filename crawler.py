import requests
from bs4 import BeautifulSoup

def csrf_scanner(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    forms = soup.find_all('form')
    for form in forms:
        csrf_token = form.find('input', {'name': 'csrf_token'})
        if not csrf_token:
            print(f"CSRF vulnerability found in: {url}")

# Example usage
url = 'https://www.facebook.com'
csrf_scanner(url)
