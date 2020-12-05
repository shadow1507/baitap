import csv
import mysql.connector
myDB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Customers"
)

with open('customer.csv') as csv_File:
    csvfile=csv.reader(csv_File, delimiter=',')
    all_values=[]
    for row in csvfile:
        values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12])

        if row[0] =='customerid':
            continue
        all_values.append(values)
query = " INSERT INTO customer(customerid, firstname, lastname, companyname, billingaddress1, billingaddress2, city, state, postalcode, country, phonenumber, emailaddress, createddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
mycursor= myDB.cursor()
mycursor.executemany(query,all_values)
myDB.commit()