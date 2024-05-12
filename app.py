import time
import threading
import multiprocessing as mp
import requests
import random
from bs4 import BeautifulSoup
import mysql.connector
import re

from requests_ip_rotator import ApiGateway, EXTRA_REGIONS, ALL_REGIONS
# import mydatabase 
import urllib3
from flask import Flask

app = Flask(__name__)


def specific_string(length):
    # define the specific string
    sample_string = 'pqrstuvwxyaksdjhkasdlkjqluwoelkansldknc'
    # define the condition for random string
    result = ''.join((random.choice(sample_string)) for x in range(length))
    return result

def trace_id(length):
    # define the specific string
    sample_string = 'pq0rstu1vw2xya3ksdj4hkasdl5kjql6uwo7el8kansl9dknc'
    # define the condition for random string
    result = ''.join((random.choice(sample_string)) for x in range(length))
    
    return result
    



cookies = {
    'session-id': '258-5965937-1481739',
    'session-id-time': '2082787201l',
    'i18n-prefs': 'INR',
    'ubid-acbin': '262-9353634-4686744',
    'session-token': 'LkNzzq+EbJ1DBY9a422qj/Nj51jhUkvavH+WeGlHA9esFkV7jBg8meaewFfohOCIQlRH015Up/bMNJNiH5RDDZHsn3JzNWf2d8EF8CPDCs64uglTEN+WzYIVCFePEBxYWuszo//2ORnWB90Mf6vwt5AwexTyyzuAEfMw6+h7g/5VeJ9Vf4n2AOOArPVfWEo0/X32T/I0J5FsY1QY64xyY1Am6gnpLp2E59cyantZtxN/FBb5f9TmFhWMhuH78gv1Mg39uNWqkXvEv8EOpjEbClbgsbqkovV9gjrvjjYDUAqvVDft/kiX16VOuOYlAiAtGfcTuVRd6taD8lzsBYqeG6Sc7Js40Cg/',
    'csm-hit': 'tb:s-RCA08544A2YQCT2J63XM|1684211284757&t:1684211285532&adb:adblk_no',

}

headers = {
    'User-Agent': specific_string(random.randint(1, 999)),
    'From': specific_string(random.randint(1, 999)),
    'Referer': "https://www.amazon.in/",
    
    
}



def scrape_page(url):

    
    # Scrape the page and return the data

    # Create gateway object and initialise in 
    
    
    key_id = 'AKIAQ3EGRB3CWDYAIVRP'
    secret_key = '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'
    
    
    gateway = ApiGateway(url,access_key_id=key_id,access_key_secret=secret_key)
    gateway.start()

    session = requests.Session()
    session.mount(url, gateway)

    
    webpage = session.get(url, headers=headers,cookies=cookies,params={"theme": "light"})
    soup = BeautifulSoup(webpage.text, "html.parser")
    
     
    print(webpage.status_code)
    # # Delete gateways
    # gateway.shutdown()


    all_title = []
    try:
        # Outer Tag Object
        title = soup.find("span",
                          attrs={"id": 'productTitle'})

        # Inner NavigableString Object
        title_value = title.string

        # Title as a string value
        title_string = title_value.strip().replace(',', '')

    except AttributeError:
        title_string = "NA"

    # print("product Title = ", title_string)

    # saving the title in the file
    all_title.append(title_string)
    # File.write(f"{title_string},")

    # retrieving product color--------------------------------------------------
    all_colors = []
    for li in soup.find_all("img", attrs={'class': 'imgSwatch'}):
        all_colors.append(li['alt'])

        #  price ---------------------------------------------------------
    all_price = []
    try:
        price = soup.find(
            "span", attrs={'class': 'a-price-whole'}).string.strip().replace(',', '')
        # we are omitting unnecessary spaces
        # and commas form our string
    except AttributeError:
        price = "NA"
    # print("Products price = ", price)

    # saving
    # File.write(f"{price},")
    all_price.append(price)


    # retrieving product discount------------------------------------------
    all_discount = []
    try:
        discount = soup.find("div", attrs={
            'class': 'a-section '}).string.strip().replace(',', '')

    except AttributeError:

        try:
            discount = soup.find(
                "span", attrs={'class': 'a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage'}).string.strip().replace(',', '')
        except:
            discount = "NA"
        all_discount.append(discount)
        # File.write(f"{discount},")

    # print("discount = ", discount)

    # retrieving product size--------------------------------------------------

    all_size = []
    size = soup.select_one(
        'select[name="dropdown_selected_size_name"]').select('option')
    size.pop(0)
    for op in size:

        all_size.append(op.get_text())
        # print(op.get_text())
    # File.write(f"{op.get_text()},")

 # retrieving product rating------------------------------------------------

    all_rating = []
    try:
        rating = soup.find("i", attrs={
            'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')

    except AttributeError:

        try:
            rating = soup.find(
                "span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
        except:

            rating = "NA"
    all_rating.append(rating)
#   print("Overall rating = ", rating)

# print availablility status-----------------------------------------------

    all_avel = []
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip().replace(',', '')

    except AttributeError:
        available = "NA"
#   print("Availability = ", available)

    # saving the availability and closing the line
    all_avel.append(available)
    # File.write(f"{available},\n")

    # closing the file
    # Delete gateways
    time.sleep(10)
    # File.close()
    listdata = [all_colors, all_title,all_discount, all_rating, all_avel, all_price,all_size]
    
    
    return listdata
    
   
class ThreadedScraper(threading.Thread):
    def __init__(self, urls):
        super().__init__()
        self.urls = urls
        return "ok"

    def run(self):
        for url in self.urls:
            data = scrape_page(url)
            return "ok"
            # Process the scraped data


def scrape_pages_mp(urls):
     with mp.Pool(10) as p:
        results = p.map(scrape_page, urls)
        

       
     return results


@app.route('/output')
def gss():
 
    urls = {

        "https://www.amazon.in/dp/B08PRXXQB3",
        "https://www.amazon.in/dp/B01MTQ5M7B",
        "https://www.amazon.in/dp/B0BT1FJCWW",
        "https://www.amazon.in/dp/B0CGD8HGCJ",
        "https://www.amazon.in/dp/B0BT1FJCWW",
        "https://www.amazon.in/dp/B0CGD8HGCJ",
       
        
        
        
        
       
    }
    
    

    # Test the multiprocessed scraper

    start = time.time()
    data = scrape_pages_mp(urls)
    
    time.sleep(10)
    end = time.time()
    print(f"Time taken for multiprocessed scraper: {end - start} seconds")
    
    return data
    

    
if __name__ == "__main__":

    app.run() 
