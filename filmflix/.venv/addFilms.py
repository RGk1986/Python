from connect import *

# Create an insert function (User Input Method)
def insertData():
    title = input("Enter the film title: ").title()
    yearReleased = input("Enter the year released: ").title()
    rating = input("Enter your rating from 1-5: ")
    duration = input("Enter the duration in minutes: ")
    genre = input("Enter the genre: ").title()
    
    dbCursor.execute("INSERT INTO tblFilms VALUES (NULL, ?, ?, ?, ?, ?)", (title, yearReleased, rating, duration, genre))
    dbCon.commit() # commit the changes to the database, permanently adding the song to the table
    
    print(f"{title} added to the database at filmID {dbCursor.lastrowid}")

if __name__ == "__main__":
    insertData()