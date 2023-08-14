from connect import *

# create a function 
def updateData():
    # use primaryKey to update a record
    idField = input("Enter the id of the record you want to update: ")

    # Title, Artist, Genre. 
    titleField = input("Enter Title of song: ").title()
    artistField = input("Enter Artist name: ").title()
    genreField = input("Enter Genre of song: ").title()

    titleField = f"'{titleField}'"
    artistField = f"'{artistField}'"
    genreField = f"'{genreField}'"

    dbCursor.execute(f"UPDATE songs SET Title = {titleField}, Artist = {artistField}, Genre = {genreField} where songID = {idField}")
    dbCon.commit()
    print(f"Record {idField} updated successfully in the songs table value is now {titleField}, performed by {artistField}, it is a {genreField} song")


if __name__ == "__main__":
    updateData()
