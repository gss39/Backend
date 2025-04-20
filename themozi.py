
# Importing libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import themozi_database
import re
import csv
import sqlite3
import time
import mysql.connector
# # Intializing driver
driver = webdriver.Chrome()

price_1 = []
name_1 = []
rating_1 = []
mrp_1 = []
colors_1 = []
# discount_1 = []
saller = "Flipkert"

urls = []
for i in themozi_database.fetch_data():
    link = i
    urls.append(link)

id_links = []
product_id = themozi_database.fetch_data()
for li in product_id:
    id_links.append(li)

pro_link = []

# URL to fetch from Can be looped over / crawled multiple urls
for ul in urls:
    driver.get(ul)
    # if ul == "https://thenmozhidesigns.com/products/blue-velvet-blue-mangalagiri-plain-cotton-saree-copy":
    #     break
    
    pro_link.append(ul)

    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
  
    try:
     for title in soup.findAll('h1', attrs={'class': 'product-title h3'}):
       title1 = title.text
        # print(title.text)
    except:
        title1 =  "NA"
    name_1.append(title1)


    cols =  []
    # try:
    for colors in soup.findAll('div', attrs={'data-block-id': 'product_variations_GeijNk'}):
      
      
        
        cols.append(colors.text)

        # color_list = map(str, cols)
        # color ='!'.join(color_list)
        # colors_1.append(color)
        print(cols)
         
        # if colors == 'NULL':
        #   print("not")
        # if colors != 'NULL':
        #    print("yes")

        #  print(colors1)
    # except:
    #     colors1 =  "NA"
    # colors_1.append(colors1)


    mrp_pr = []
    try:
     for price_mrp in soup.findAll('price-list', attrs={'class': 'price-list price-list--product'}):

        gss = price_mrp.text
        pr_mr = gss.split()
        mrp_pr.append(pr_mr)
    
     price = mrp_pr[0][2]
    except:
      price = "NA"
    price_1.append(price)

    try:
     if len(mrp_pr[0]) == 3:

        mrp = price

     if len(mrp_pr[0]) == 6:

        mrp = mrp_pr[0][5]
    except:
      mrp = "NA"
    mrp_1.append(mrp)

    
    
    for rating in soup.findAll('span', attrs={'class':'smallcaps text-xxs text-subdued'}):
      rating1 = rating.text
    
      
        #  print(rating.text)
    rating_1.append(rating1)
    rate = rating_1[0]

    data = [name_1, price_1, mrp_1, rating_1,colors_1]
    # print(data)


    # with open('themozi.csv', newline='', encoding='utf-8') as csvfile:
    #  reader = csv.DictReader(csvfile)  # Assuming first row contains headers
    #  for row in reader:
       
    #     myname = row['name']  # Adjust field names to match CSV headers
    #     myprice= row['price']
    #     mymrp = row['mrp']
    #     myrating= row['Rating']
    #     p_ids = row['product_id']

  

    #     mydb = mysql.connector.connect(

    #      host="localhost",
    #      user="root",
    #      password="",
    #      database="mydatabase"

    #     # host="localhost",
    #     # user="root",
    #     # password="brandonly!@#",
    #     # database="egxcmgbg_ecomrce_website"
    #      )

    #     mycursor = mydb.cursor()

    #     sql = "UPDATE `products` SET `title`='"+myname+"',`rating`='"+myrating + \
    #     "',`price`='"+myprice+"',`mrp`='" + \
    #     mymrp+"' WHERE p_link ='"+p_ids+"'"
    #     mycursor.execute(sql)

    #     mydb.commit()
    #     print("1 record inserted, ID:", mycursor.lastrowid)


    #     df = pd.DataFrame({"name":name_1,"price":price_1,"mrp":mrp_1,"Rating":rating1,"product_id":pro_link})
    #     df.to_csv("themozi2.csv", index=True)

    print("Data updated successfully.")

# # Create a DataFrame from the extracted data and Save the DataFrame to a CSV file.
