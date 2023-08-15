from connect import *

def reportAll():
    dbCursor.execute("SELECT * FROM tblFilms")
    print(dbCursor.fetchall())

if __name__ == "__main__":
    reportAll()

def reportGenre():
    genreNeed = input("Enter a genre: ").title()
    dbCursor.execute("SELECT * FROM tblFilms WHERE genre = ?", (genreNeed,))
    print(dbCursor.fetchall())

if __name__ == "__main__":
    reportGenre()
    
def reportYear():
    yearNeed = input("Enter a year: ")
    dbCursor.execute("SELECT * FROM tblFilms WHERE year = ?", (yearNeed,))
    print(dbCursor.fetchall())
    
if __name__ == "__main__":
    reportYear()

def reportRating():
    ratingNeed = input("Enter a rating: ")
    dbCursor.execute("SELECT * FROM tblFilms WHERE rating = ?", (ratingNeed,))
    print(dbCursor.fetchall())

if __name__ == "__main__":
    reportRating()
    
