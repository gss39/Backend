
# Importing libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import meesho_database
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

urls = []
for i in meesho_database.fetch_data():
    link = "https://www.meesho.com/new-fency-georgette-cut-work-saree/p/"+i+""
    urls.append(link)


id_links = []
product_id = meesho_database.fetch_data()
for li in product_id:
    id_links.append(li)


# URL to fetch from Can be looped over / crawled multiple urls
for ul in urls:
    driver.get(ul)

    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    try:
     for price in soup.findAll('h4', attrs={'class': 'sc-eDvSVe biMVPh'}):
        pr = price.text
        print(pr)
    except:
        pr = "NA"
    price_1.append(pr)

    try:
     for name in soup.findAll('span', attrs={'class': 'sc-eDvSVe fhfLdV'}):
        nm = name.text
        print(nm)
    except:
        nm = "NA"
    name_1.append(nm)

    try:
     for rating in soup.findAll('h1', attrs={'class': 'sc-eDvSVe cdZTwf'}):
        rt = rating.text
        print(rt)
    except:
        rt = "NA"
    rating_1.append(rt)

print(rating_1, name_1, price_1)


for item1, item2, item3, item5 in zip(price_1, name_1, rating_1, id_links):
    all = [item1, item2, item3, item5]
    title = re.sub("[!@#$%^&*...']", " ", all[1])

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

    sql = "UPDATE `products` SET `title`='"+title+"',`rating`='"+all[2] + \
        "',`price`='"+all[0]+"' WHERE product_id ='"+all[3]+"'"
    mycursor.execute(sql)

    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)

    # df = pd.DataFrame({"name":name_1,"price":price_1,"mrp":mrp_1,"Rating":rating_1,"discount":discount_1,"colors":color})
    # df.to_csv("flipkart.csv", index=True)

print("Data updated successfully.")


# for mrp in soup.findAll('p', attrs={'class':'sc-bqWxrE dOoCNY'}):

#     print(mrp.text)
#     mrp_1.append(mrp.text)


# for colors in soup.findAll('div', attrs={'class':'V3Zflw QX54-Q E1E-3Z dpZEpc'}):

#     print(colors.text)
#     colors_1.append(colors.text)

# for discount in soup.findAll('div', attrs={'class':'UkUFwK WW8yVX dB67CR'}):

#     print(discount.text)
#     discount_1.append(discount.text)

# color_list = map(str, colors_1)
# color = '!'.join(color_list)

# Create a DataFrame from the extracted data and Save the DataFrame to a CSV file.

# df = pd.DataFrame({"name":name_1,"price":price_1,"mrp":mrp_1,"Rating":rating_1,"discount":discount_1,"colors":color})
# df.to_csv("flipkart.csv", index=True)


# print("Data appended successfully.")
