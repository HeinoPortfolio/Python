# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:44:11 2019

@author: Matthew Heino
Class:   IS 362 Project 3
"""

import pandas as pd
from sqlalchemy import create_engine


pd.set_option('display.max_columns', None)


connection_string = "mysql+pymysql://root:slice457@localhost:3306/chinook"

db_query = 'SELECT customer.LastName, customer.FirstName, track.Name , album.Title FROM Customer JOIN invoice ON customer.CustomerId = invoice.CustomerId JOIN invoiceline ON invoice.InvoiceId = invoiceline.InvoiceId JOIN track ON invoiceline.TrackId = track.TrackId JOIN album ON track.AlbumId = album.AlbumId ORDER BY customer.LastName;'
db_connection = create_engine(connection_string)

print (db_connection)


music_frame = pd.read_sql_query(db_query, con=db_connection)

music_frame.rename(columns={"LastName": "Last Name", "FirstName":"First Name"}, inplace=True)

print(music_frame.head())

#Write dataframe to CSV.
music_frame.to_csv("jupyter.csv", index=False)

#Read csv to frame

input_music_frame = pd.read_csv("jupyter.csv")
print(input_music_frame.head(20))






