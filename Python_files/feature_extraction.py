import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re
import requests

#Function to get the title of the book
def get_title(soup_detail):
    try:
        title = soup_detail.find("h1", {"id":"bookTitle"}).text.replace("\n","").replace("      ","")
    except:
        title = np.nan
    return title


#get the book author
def get_author(soup_detail):
    try:
        author = soup_detail.find("div", {"class":"authorName__container"}).text.replace("\n","")
    except:
        author = np.nan
    return author


# get ratings
def get_rating(soup_detail):
    try:
        rating = soup_detail.find("meta", {"itemprop":"ratingCount"}).text.replace("\n","").split()
        rating = rating[0]        
    except:
        rating = np.nan      
    return rating


# get avgratings
book_avgratings = []
def get_avgrating(soup_detail):
    try:
        avgrating = soup_detail.find("span", {"itemprop":"ratingValue"}).text.replace("\n","").replace(' ','')
    except:
        avgrating = np.nan
    return avgrating


# get pages
book_pages = []
def get_page(soup_detail):
    try:
        page = soup_detail.find("span", {"itemprop":"numberOfPages"}).text.split()
        page = page[0]
    except:
        page = np.nan
    return page


# get years
book_publish_year = []
def get_year(soup_detail):
    try:
        publish_year = soup_detail.find("nobr", {"class":"greyText"}).text.replace("\n","").replace(")","").split()
        publish_year = publish_year[-1]
    except:
        publish_year = np.nan
    return publish_year


# get award
def get_award(soup_detail):
    try:
        award = soup_detail.find("div", {"itemprop":"awards"}).text.replace("\n","")
    except:
        award = np.nan
    return award


# get genres
def get_genres(soup_detail):
    try:
        genres = soup_detail.find_all(class_="actionLinkLite bookPageGenreLink")
        genres = genres[:3]
        genres = [genre.get_text() for genre in genres]
    except:
        genres = np.nan
    return genres


#get the book reviews
def get_review(soup_detail):
    try:
        review = soup_detail.find("meta", {"itemprop":"reviewCount"}).text.replace("\n","").split()
        review = review[0]
    except:
        review = np.nan
    return review


# get series
def get_series(soup_detail):
    try:
        series = soup_test.find(id="bookSeries").text.strip()
        if len(series) == 0:
            return False
        else: 
            return True
    except:
        series = np.nan
    #return series

# get places
def get_places(soup_detail):
    try:
        places = soup_test.find("div", {'id':"bookDataBox"}).find('span',class_="darkGreyText").text.replace("(","").replace(")","").strip()
    except:
        places = np.nan
    return places