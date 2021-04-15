import pandas as pd

def preprocessing(csv_path):
    df = pd.read_csv(csv_path)
    # drop na if needed add more columns
    df = df.dropna(subset=['awards'])
    df =df.dropna(subset=['original_publish_year'])
    #cleaning the data
    # cleaning data
    df['num_reviews'] = df['num_ratings'].str.replace(",","")
    df['num_ratings'] = df['num_ratings'].str.replace(",","")
    df['num_pages'] = df['num_pages'].astype(int)
    df['original_publish_year'] = df['original_publish_year'].astype(int)
    #awards count
    df['awards_count'] = [award.split(',') for award in df['awards']]
    df['awards_count'] = [len(award) for award in df['awards_count']]
    # normalization
    # 1+(rating - min/ max - min)*9
    max_avgrating=max(df['avg_rating'])

    min_avgrating=min(df['avg_rating'])

    df['mean_norm_ratings'] = round(1+((df['avg_rating']-min_avgrating)/(max_avgrating-min_avgrating))*9,2)
    df.to_csv("df_cleaned.csv", index=False)

    # preprocessing("df_new_1100.csv")