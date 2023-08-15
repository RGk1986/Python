from connect import *

def deleteData():
    # use primary  key to update a record 
    idField = input("Enter the FilmID of the record to be deleted: ")
    
    # Delete from the songs table where SongID is matched.
    dbCursor.execute(f"DELETE from tblFilms where filmID = {idField}")
    dbCon.commit()
    print(f"Successfully deleted {idField} from the songs table.")

if __name__ == "__main__":
    deleteData()