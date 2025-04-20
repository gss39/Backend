
# Importing libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import blocksand_database
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
# colors_1 = []
# discount_1 = []
saller = "Flipkert"

urls = []
for i in blocksand_database.fetch_data():
    link = i
    urls.append(link)

id_links = []
product_id = blocksand_database.fetch_data()
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
     for title in soup.findAll('h2', attrs={'class': 'single_product__title pr--block h4'}):
       title1 = title.text
        # print(title.text)
    except:
        title1 =  "NA"
    name_1.append(title1)


    price = []
    try:
     for price in soup.findAll('div', attrs={'id': 'single_product__price-template--15883506385078__main'}):

        myprice = price.text
        mr2 =  re.sub('Rs.', '', myprice)
        # pr_mr = mr2.split()
        
        # pr = pr_mr[1]
        print(mr2)
        # price_1.append(price)
    
    #  price1 = price[0][2]
    except:
      mr2 = "NA"
    price_1.append(mr2)
    
    mrp1 = mr2
    # try:
    #  if len(mrp_pr[0]) == 3:

    #     mrp = price

    #  if len(mrp_pr[0]) == 6:

    #     mrp = mrp_pr[0][5]
    # except:
    #   mrp = "NA"
    mrp_1.append(mrp1)

    
    
    for rating in soup.findAll('span', attrs={'class':'spr-badge-count'}):
      rating1 = rating.text
    
      
        #  print(rating.text)
    rating_1.append(rating1)
    rate = rating_1[0]

    data = [name_1, price_1, mrp_1, rating_1]
    print(data)


    with open('blocksand.csv', newline='', encoding='utf-8') as csvfile:
     reader = csv.DictReader(csvfile)  # Assuming first row contains headers
     for row in reader:
       
        myname = row['name']  # Adjust field names to match CSV headers
        myprice= row['price']
        mymrp = row['mrp']
        myrating= row['Rating']
        p_ids = row['product_id']

  

        mydb = mysql.connector.connect(

         host="localhost",
         user="root",
         password="",
         database="mydatabase"

        # host="localhost",
        # user="root",
        # password="brandonly!@#",
        # database="egxcmgbg_ecomrce_website"
         )

        mycursor = mydb.cursor()

        sql = "UPDATE `products` SET `title`='"+myname+"',`rating`='"+myrating + \
        "',`price`='"+myprice+"',`mrp`='" + \
        mymrp+"' WHERE p_link ='"+p_ids+"'"
        mycursor.execute(sql)

        mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)


    # df = pd.DataFrame({"name":name_1,"price":price_1,"mrp":mrp_1,"Rating":rating1,"product_id":pro_link})
    # df.to_csv("blocksand.csv", index=True)

print("Data updated successfully.")

# # Create a DataFrame from the extracted data and Save the DataFrame to a CSV file.
