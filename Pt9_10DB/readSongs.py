from connect import *

# Create a function to read the records in the songs table

def read_data():
    dbCursor.execute("SELECT * FROM songs") # Select all records from the songs table
    
    allSongs = dbCursor.fetchall() # fetchall() method returns all rows of a query result set as a list of tuples.
    
    for eachSong in allSongs: # iterate through the list of tuples
        print(eachSong) # print each tuple in the list of tuples


if __name__ == "__main__":
    read_data() # call the read_data() function