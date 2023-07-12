import psycopg2
import os
from postgres_settings import postgres_settings1 as settings

# connect to "chinook" database
connection = psycopg2.connect(database=settings["db"], password=settings["pass"])

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - Select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - Select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51]) 

# Query 5 - Select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Select all the tracks where the composer is "Queen" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - Select all the tracks where the composer is "Black Sabbath" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Black Sabbath"])

# Query 8 - Select all the tracks where the composer is "test" from the "Track" table - This is supposed to throw an error
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])

# fetch the results (multiple)
results = cursor.fetchall()

#fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)