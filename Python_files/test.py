from preprocessing import preprocessing
import pandas as pd
df = pd.read_csv('../df_1100.csv')
print(df.head())
df_cleaned = preprocessing(df)