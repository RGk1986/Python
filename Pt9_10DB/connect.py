import sqlite3 as sql # Import the sqlite3 module and rename it as sql for ease of use

# To use the sqlite3(sql) module: create a DB connection object, create a cursor object, execute SQL statements, commit changes, close connection
dbCon = sql.connect('Pt9_10DB/GLAW4C6.db') # create or open a db if one exists. 

# Create a cursor object(variable) and pass/assign it to the cursor method
dbCursor = dbCon.cursor() # cursor() method creates a cursor object