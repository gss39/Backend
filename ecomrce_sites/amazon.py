
# Importing libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import ama_database
import mysql.connector
import time
import re
# # Intializing driver
driver = webdriver.Chrome()

price_1=[]
name_1=[]
rating_1=[]
mrp_1=[]
colors_1=[]
discount_1=[]

urls =[]
for i in ama_database.fetch_data():
 link  = "https://www.amazon.in/MUNIR-Womens-Unstiched-Festival-Function/dp/"+i+""
 urls.append(link)

links = []
all_links = ama_database.fetch_data()
for li in all_links:
      links.append(li)




# URL to fetch from Can be looped over / crawled multiple urls
for ul in urls:
    driver.get(ul)
    # if ul == "https://www.amazon.in/MUNIR-Womens-Unstiched-Festival-Function/dp/B0C5SXFRTK": 
    #   break


    content = driver.page_source
    soup = BeautifulSoup(content,"html.parser")
    
    try:
     for price in soup.find('span', attrs={'class':'aok-offscreen'}):
      a = price
      pr =  a.split(".")
      new_price = pr[0]
    except:
     new_price = "NA"
    print(new_price) 
    price_1.append(new_price)
  
    try: 
     for name in soup.find('span', attrs={'id':'productTitle'}):
      print(name)   
    except:
        name = "NA"
    print(name)
    name_1.append(name)

   

    try: 
     for rating in soup.find('span', attrs={'class':'a-size-base a-color-base'}):
      print(rating)
    except:
        rating = "NA" 
    print(rating)
    rating_1.append(rating)


    try:
     for mrp in soup.find('span', attrs={'class':'a-size-small aok-offscreen'}):
        a = mrp
        pr =  a.split(":")
        new_mrp = pr[1]
        
    except:
      new_mrp = "NA"
    print(new_mrp)
    mrp_1.append(new_mrp)
    # # for colors in soup.findAll('div', attrs={'class':'V3Zflw QX54-Q E1E-3Z dpZEpc'}):

    # #     print(colors.text)
    
    
    try:
      for discount in soup.find('span', attrs={'class':'a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage'}):
         print(discount)
    except:
      discount = "NA"
    print(discount)
    discount_1.append(discount)


all_detals = []
mydata = [price_1, name_1, rating_1, mrp_1, discount_1]

for i in mydata:

  all_detals.append(i)
  
# for j in all_detals:
#   print(j)
  
  
# for item1 , item2 in zip (links,all_detals):
#   all = [item1,item2] 
mydata = []
for item1, item2, item3, item5, item6, item7 in zip(all_detals[0], all_detals[1], all_detals[2], all_detals[3], all_detals[4], links):
  all = [item1, item2, item3, item5, item6, item7]
  mydata.append(all)

  print()
  titles = all[1]
  discount = all[4]
  price = all[0]

  title =  re.sub("[!@#$%^&*...']", " ", titles)
  discounts =  re.sub("[%-]", " ", discount)
  prices =  re.sub("[₹]", " ", price)
 
  df = pd.DataFrame({"name":all_detals[0],"price":price_1,"mrp":mrp_1,"Rating":rating_1,"discount":discount_1})
  df.to_csv("amazon.csv", index=True)
  pro_data = [price_1,name_1,rating_1,mrp_1,colors_1,discount_1]
# # print(pro_data)

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

  sql = "UPDATE `products` SET `title`='"+title+"',`discount`='"+all[4]+"',`rating`='"+all[2] + \
        "',`price`='"+prices+"',`mrp`='" + \
        all[3]+"' WHERE product_id ='"+item7+"'"
  mycursor.execute(sql)

  mydb.commit()
  print("1 record inserted, ID:", mycursor.lastrowid)


   

    
   

# print("Data updated successfully.")
