import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
URL = os.getenv('URL')
DIARY_LOGIN = os.getenv('DIARY_LOGIN')
DIARY_PASSWORD = os.getenv('DIARY_PASSWORD')


payload = {
        "login": DIARY_LOGIN,
        "password": DIARY_PASSWORD
}

session_requests = requests.session()
result = session_requests.post(URL, data = payload, headers = dict(referer = URL))

    # Scrape journal_url
result = session_requests.get(URL, headers = dict(referer = URL))
soup = BeautifulSoup(result.content)
print(soup.prettify())