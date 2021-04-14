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


        title.append(get_title(soup_detail))
        author.append(get_author(soup_detail))
        num_reviews.append(get_review(soup_detail))
        num_ratings.append(get_rating(soup_detail))
        avg_rating.append(get_avgrating(soup_detail))
        num_pages.append(get_page(soup_detail))
        original_publish_year.append(get_year(soup_detail))
        series.append(get_series(soup_detail))
        genres.append(get_genres(soup_detail))
        awards.append(get_award(soup_detail))
        places.append(get_places(soup_detail))
        
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