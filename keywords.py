
# Importing libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
# import meesho_database
import time
import re
import mysql.connector
# # Intializing driver
driver = webdriver.Chrome()

price_1 = []
name_1 = []
rating_1 = []
mrp_1 = []
colors_1 = []
discount_1 = []

# urls = []
# for i in meesho_database.fetch_data():
#     link = "https://www.google.com/search?q=saree&oq=sare&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDkyBggCEEUYPDIGCAMQRRg8MgYIBBBFGDzSAQg0MTU5ajBqMagCALACAA&sourceid=chrome&ie=UTF-8&sei=T58DaLCNOeuK4-EPpMTsYQ"
#     urls.append(link)


# id_links = []
# product_id = meesho_database.fetch_data()
# for li in product_id:
#     id_links.append(li)


# URL to fetch from Can be looped over / crawled multiple urls
# for ul in urls:
driver.get("https://www.google.com/search?q=saree&oq=sare&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDkyBggCEEUYPDIGCAMQRRg8MgYIBBBFGDzSAQg0MTU5ajBqMagCALACAA&sourceid=chrome&ie=UTF-8&sei=T58DaLCNOeuK4-EPpMTsYQ")
time.sleep(15)
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")


for price in soup.findAll('span', attrs={'class': 'dg6jd'}):
    pr = price.text
    print(pr)
    

    # try:
    #  for name in soup.findAll('span', attrs={'class': 'sc-eDvSVe fhfLdV'}):
    #     nm = name.text
    #     print(nm)
    # except:
    #     nm = "NA"
    # name_1.append(nm)

    # try:
    #  for rating in soup.findAll('h1', attrs={'class': 'sc-eDvSVe cdZTwf'}):
    #     rt = rating.text
    #     print(rt)
    # except:
    #     rt = "NA"
    # rating_1.append(rt)



