
import links_extraction as le
import scrap_and_save as s_s

"""Order of Execution will be,
1. links_extraction
2. feature_extraction
3. scrap_data

5. if anything left, we can include it in scraper """

list_of_1000_links = le.get_all_1000_links('https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century?page=')
df =s_s.create_df_and_save_as_csv(list_of_1000_links)

#### other version
df = s_s.create_df_and_save_as_csv(le.get_all_1000_links('https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century?page='))