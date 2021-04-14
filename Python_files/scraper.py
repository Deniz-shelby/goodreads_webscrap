import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re
import requests
import links_extraction
import feature_extraction

"""Order of Execution will be,
1. links_extraction
2. feature_extraction
3. pre-processing 
4. plots

5. if anything left, we can include it in scraper """

