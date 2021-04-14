import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re
import requests


url = requests.get("https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century?page=1")
soup = BeautifulSoup(url.content, 'html.parser')

print(soup)