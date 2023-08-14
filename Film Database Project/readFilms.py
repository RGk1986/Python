from connect import *

def readData():
    dbCursor.execute('SELECT * FROM tblFilms')
    
    allFilms = dbCursor.fetchall()
    
    for eachFilm in allFilms:
        print(eachFilm)

if __name__ == "__main__":
    readData()