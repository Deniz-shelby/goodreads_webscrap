import feature_extraction as fe
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests

def create_df_and_save_as_csv(url_list):
    title = []
    author = []
    num_reviews = []
    num_ratings = []
    avg_rating = []
    num_pages = []
    original_publish_year = []
    series = []
    genres = []
    awards = []
    places = []
    
    for link in url_list:
        one_book= requests.get(link)
        soup_detail = BeautifulSoup(one_book.content, 'html.parser')


        title.append(fe.get_title(soup_detail))
        author.append(fe.get_author(soup_detail))
        num_reviews.append(fe.get_review(soup_detail))
        num_ratings.append(fe.get_rating(soup_detail))
        avg_rating.append(fe.get_avgrating(soup_detail))
        num_pages.append(fe.get_page(soup_detail))
        original_publish_year.append(fe.get_year(soup_detail))
        series.append(fe.get_series(soup_detail))
        genres.append(fe.get_genres(soup_detail))
        awards.append(fe.get_award(soup_detail))
        places.append(fe.get_places(soup_detail))
        
    data = {'url' : url_list,
            'title':title,
            'author':author,
            'num_reviews':num_reviews,
            'num_ratings': num_ratings,
            'avg_rating':avg_rating,
            'num_pages':num_pages,
            'original_publish_year':original_publish_year,
            'series':series,
            'genres':genres,
            'awards':awards,
            'places':places
           }
    df = pd.DataFrame(data)
    df.to_csv("df_new_100o.csv", index=False)