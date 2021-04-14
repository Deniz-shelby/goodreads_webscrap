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

list_of_10pages = get_list_pages_of_10('https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century?page=')
#print(list_of_10pages)

#Function to get the 100 links (links of 100 books) in one page
def get_links_for_100(url_one_page):
    url_page = requests.get(url_one_page)
    soup = BeautifulSoup(url_page.content, 'html.parser')
    href_link_list =[]
    for link in soup.find_all('a', class_='bookTitle') :
        if link.has_attr('href'):
            href_link_list.append(link.attrs['href'])
    return href_link_list

list_of_100_links = get_links_for_100('https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century?page=1')
#print(len(list_of_100_links))
#print(list_of_100_links[0])

""" The function get_link_for_100 retreives the links for links of all books in a page,
However the links cannot be opened as they are book specific and doesnot contain the website tag.
So, in the following function we create the full link """


def get_url_from(url_list_from_get_links):
    list_container = []
    for i in range(0,100):
        url_detail = "https://www.goodreads.com" + str(list_of_100_links[i])    
        list_container.append(url_detail)
    return list_container

url_of_100 = get_url_for_goodreads_from_list(list_of_100_links)
#print(url_of_100)