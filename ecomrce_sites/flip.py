
# Importing libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import flip_database
import time
import mysql.connector
# # Intializing driver
driver = webdriver.Chrome()

price_1 = []
name_1 = []
rating_1 = []
mrp_1 = []
colors_1 = []
discount_1 = []
saller = "Flipkert"

urls = []
for i in flip_database.fetch_data():
    link = "https://www.flipkart.com/rajlaxmi-fashion-flared-a-line-gown/p/itm148004537951f?pid="+i+""
    urls.append(link)

id_links = []
product_id = flip_database.fetch_data()
for li in product_id:
    id_links.append(li)


# URL to fetch from Can be looped over / crawled multiple urls
for ul in urls:
    driver.get(ul)
    # if ul == "https://www.flipkart.com/rajlaxmi-fashion-flared-a-line-gown/p/itm148004537951f?pid=SARGZ7FH2PGRQF6T": 
    #   break

    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    try:
     for price in soup.findAll('div', attrs={'class': 'Nx9bqj CxhGGd'}):
        pr = price.text
        print(pr)
    except:
        pr = "NA"
    price_1.append(pr)

    try:
     for name in soup.findAll('span', attrs={'class': 'VU-ZEz'}):
        nm = name.text
        print(nm)
    except:
        nm = "NA" 
    name_1.append(nm)
     
    try:  
     for rating in soup.findAll('div', attrs={'class': 'XQDdHH _1Quie7'}):
        rt = rating.text
        
        print(rt)
    except:
        rt = "NA" 
        
    rating_1.append(rt)

    try:
     for mrp in soup.findAll('div', attrs={'class': 'yRaY8j A6+E6v'}):
        mr = mrp.text
        print(mr)
    except:  
        mr =  "NA" 
    mrp_1.append(mr)

    # for colors in soup.findAll('div', attrs={'class': 'V3Zflw QX54-Q E1E-3Z dpZEpc'}):

        # color_list = map(str, colors)
        # color = '!'.join(color_list)
        # colors_1.append(color)
        # print(color)
    try:
     for discount in soup.findAll('div', attrs={'class': 'UkUFwK WW8yVX dB67CR'}):
        dis = discount.text
        print(dis)
    except:  
         dis = "NA"  
    discount_1.append(dis)




all_detals = []
mydata = [price_1, name_1, rating_1, mrp_1, discount_1]

for i in mydata:

  all_detals.append(i)


# print(pro_data)
all_data = []
for item1, item2, item3, item5, item6, item8 in zip(all_detals[0], all_detals[1], all_detals[2], all_detals[3], all_detals[4], id_links):
    all = [item1, item2, item3, item5, item6, item8]
    
    all_data.append(all)
    

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

    sql = "UPDATE `products` SET `title`='"+all[1]+"',`discount`='"+all[4]+"',`rating`='"+all[2]+ \
        "',`price`='"+all[0]+"',`mrp`='"+all[0]+"' WHERE product_id ='"+all[5]+"'"
    mycursor.execute(sql)

    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)


    df = pd.DataFrame({"name":name_1,"price":price_1,"mrp":mrp_1,"Rating":rating_1,"discount":discount_1})
    df.to_csv("flipkart.csv", index=True)

print("Data updated successfully.")

# # Create a DataFrame from the extracted data and Save the DataFrame to a CSV file.
