#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from pprint import pprint

response = requests.get(
    'https://peter.sh/experiments/chromium-command-line-switches')

soup = BeautifulSoup(response.text, 'html.parser')
soup.
