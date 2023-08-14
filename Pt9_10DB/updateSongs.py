from connect import *

# create a function 
def updateData():
    # use primary  key to update a record 
    idField = input("Enter the SongID of the record to be updated: ")

    #field to be updated: Title, Artist, Genre
    fieldName = input("Enter Title or Artist or Genre as field name: ").title()
    'titleField = input("Enter Title value : ").title()'
    'artistField = input("Enter Artist value : ").title()'
    'genreField = input("Enter Genre value: ").title()'

    # titleField  = "'"+titleField +"'"
    # artistField = "'"+artistField+"'"
    # genreField  = "'"+genreField +"'"

    # field Value: ask for the value for the field(Title, Artist, Genre) to be updated
    fieldValue = input(f"Enter the value for {fieldName} field: ")
    print(fieldValue)

    fieldValue = f"'{fieldValue}'"
    print(fieldValue)


    # update a record in the songs table
    dbCursor.execute(f"UPDATE songs SET {fieldName} = {fieldValue} WHERE SongID = {idField}")
    # dbCursor.execute(f"UPDATE songs SET Title = {titleField}, Artist = {artistField}, Genre = {genreField} WHERE SongID = {idField}")
    dbCon.commit()
    print(f"Record {idField} updated in the songs table.")
    
if __name__ == "__main__":
    updateData() # call or invoke the subroutine or function
