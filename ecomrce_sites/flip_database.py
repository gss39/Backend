
import mysql.connector
from flask import Flask

# app = Flask(__name__)

# @app.route('/data')
def fetch_data():

    mydb = mysql.connector.connect(
        
        host="localhost",
        user="root",
        password="",
        database="mydatabase"

        # host="localhost",
        # user="egxcmgbg_brandonly",
        # password="brandonly!@#",
        # database="egxcmgbg_ecomrce_website"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM products WHERE seller ='Flipkert'")
    myresult = mycursor.fetchall()
    
    p_id = []
    for i in myresult:
    
        data = i[1]
        p_id.append(data)
    return p_id

# if __name__ == "__main__":

#     app.run() 
    

    