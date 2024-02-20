import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import quote_plus
import os
import re
import logging

def not_lacie(href):
    return href and re.compile("/ja/cast").search(href)

def is_multiple(url):
    response = requests.get(url)
    logging.info(response.text)
    soup = BeautifulSoup(response.text)
    founds = soup.find_all("a", href=not_lacie)
    logging.info(founds)
    if (len(founds) > 3): return True
    return False
