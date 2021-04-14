import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re
import requests

#Function to get the list of pages from 1-10 in goodreads website
def get_list_pages_of_10(url_list_10):
    url_list = []
    for page_number in range(0,11):
        #remember that the end is ?page=
        url_page = url_list_10+str(page_number)
        url_list.append(url_page)
    return url_list

# function to get href 100 links
def get_links_for_100(url_one_page):
    url_page = requests.get(url_one_page)
    soup = BeautifulSoup(url_page.content, 'html.parser')
    href_link_list =[]
    for link in soup.find_all('a', class_='bookTitle') :
        if link.has_attr('href'):
            href_link_list.append("https://www.goodreads.com" + str(link.attrs['href']))
    return href_link_list

def get_links_for_100(url_one_page):
    url_page = requests.get(url_one_page)
    soup = BeautifulSoup(url_page.content, 'html.parser')
    href_link_list =[]
    for link in soup.find_all('a', class_='bookTitle') :
        if link.has_attr('href'):
            href_link_list.append("https://www.goodreads.com" + str(link.attrs['href']))
    return href_link_list