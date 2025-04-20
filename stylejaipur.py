
# Importing libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import stylejaipur_database  
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
discount_1 = []
saller = "Flipkert"

urls = []
for i in stylejaipur_database.fetch_data():
    link = i
    urls.append(link)

id_links = []
product_id = stylejaipur_database.fetch_data()
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
     for title in soup.findAll('h1', attrs={'class': 'm-product-title'}):
       title1 = title.text
        # print(title.text)
    except:
        title1 =  "NA"
    name_1.append(title1)


    price = []
    try:
     for price in soup.findAll('span', attrs={'class': 'm-price-item m-price-item--sale m-price-item--last m:text-xl md:m:text-2xl'}):

        myprice = price.text
        pr_mr = myprice.split()
        
        pr = pr_mr[1]
        # pr2 =  re.sub("[!@#$%^&*""...']", " ", pr)
        
    
    #  price1 = price[1]
    #  print(price1)
    except:
      pr = "NA"
    price_1.append(pr)

    

    
    try:
      for mrp in soup.findAll('s', attrs={'class': 'm-price-item m-price-item--regular'}):

        mymrp = mrp.text
        pr_mr = mymrp.split()
        mr = pr_mr[1]
        mr2 =  re.sub('"', ' ', mr)
        # price_1.append(price)
    
    #  price1 = price[0][2]
    except:
      mr2 = "NA"
    mrp_1.append(mr2)

    
    try:
      for discount in soup.find('span', attrs={'class':'m-currency--saved m:font-medium'}):
         print(discount)
         pr2 =  re.sub("[!@#$%^&*""...']", " ", discount)
    except:
      pr2 = "NA"
    # print(discount)
    discount_1.append(pr2)
    
    
    # for rating in soup.findAll('span', attrs={'class':'spr-badge-count'}):
    #   rating1 = rating.text
    
      
    #     #  print(rating.text)
    # rating_1.append(rating1)
    # rate = rating_1[0]

    data = [name_1, price_1, mrp_1, discount_1]
    print(data)


    with open('stylejaipur.csv', newline='', encoding='utf-8') as csvfile:
     reader = csv.DictReader(csvfile)  # Assuming first row contains headers
     for row in reader:
       
        myname = row['name']  # Adjust field names to match CSV headers
        myprice= row['price']
        mymrp = row['mrp']
        mydiscount= row['discount']
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

        sql = "UPDATE `products` SET `title`='"+myname+"',`discount`='"+mydiscount + \
        "',`price`='"+myprice+"',`mrp`='" + \
        mymrp+"' WHERE p_link ='"+p_ids+"'"
        mycursor.execute(sql)

        mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)


    # df = pd.DataFrame({"name":name_1,"price":price_1,"mrp":mrp_1,"discount":discount_1,"product_id":pro_link})
    # df.to_csv("stylejaipur.csv", index=True)

print("Data updated successfully.")

# # Create a DataFrame from the extracted data and Save the DataFrame to a CSV file.
