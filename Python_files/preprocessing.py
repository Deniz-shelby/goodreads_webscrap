import pandas as pd

def preprocessing(df_input):
    df = df_input
    # drop na if needed add more columns
    df = df.dropna(subset=['awards'])
    df =df.dropna(subset=['original_publish_year'])
    #cleaning the data
    # cleaning data
    df['num_reviews'] = df['num_reviews'].str.replace(",","")
    df['num_reviews'] = str(df['num_reviews'])
    df['num_ratings'] = df['num_ratings'].str.replace(",","")
    df['num_ratings'] = str(df['num_ratings'])
    df['num_pages'] = df['num_pages'].astype(int)
    df['original_publish_year'] = df['original_publish_year'].astype(int)
    #awards count
    df['awards_count'] = [award.split(',') for award in df['awards']]
    df['awards_count'] = [len(award) for award in df['awards_count']]
    # normalization
    # 1+(rating - min/ max - min)*9
    max_avgrating=max(df['avg_rating'])
    min_avgrating=min(df['avg_rating'])
    mean_avgrating = df['avg_rating'].mean()


    df['mean_norm_ratings'] = round(1+((df['avg_rating']-min_avgrating)/(max_avgrating-min_avgrating))*9,2)
    df['mean_norm_ratings'] = round((((df['avg_rating']-mean_avgrating)/(max_avgrating-min_avgrating))+1) * 4.5 + 1, 2)


    df.to_csv("df_cleaned.csv", index=False)
    return df
    

    # preprocessing("df_new_1100.csv")