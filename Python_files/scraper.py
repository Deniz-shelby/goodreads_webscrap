import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re
import requests
import links_extraction
import feature_extraction
import scrap_and_save

"""Order of Execution will be,
1. links_extraction
2. feature_extraction
3. scrap_data

5. if anything left, we can include it in scraper """

list_of_1000_links = get_all_1000_links('https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century?page=')
create_df_and_save_as_csv(list_of_1000_links)

#### other version
create_df_and_save_as_csv(get_all_1000_links('https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century?page='))