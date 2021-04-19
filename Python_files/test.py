import links_extraction as le
import scrap_and_save as s_s
import timeit

def main():
    list_of_1100_links = le.get_all_1000_links('https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century?page=')
    df_all =s_s.create_df_and_save_as_csv(list_of_1100_links)

if __name__=='__main__':
    main()