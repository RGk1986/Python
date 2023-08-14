from connect import *

# Create an insert function (User Input Method)
def insert_data():
    # Note SongID is Primary Key and is autoincremented
    # Ask for user input for the song title, artist and genre
    songTitle = input("Enter the song Title: ")
    songArtist = input("Enter the song Artist: ")
    songGenre = input("Enter the song Genre: ")
    # dbCursor.execute("INSERT INTO songs (Title, Artist, Genre) VALUES (?, ?, ?)", (songTitle, songArtist, songGenre))
    dbCursor.execute("INSERT INTO songs VALUES (NULL, ?, ?, ?)", (songTitle, songArtist, songGenre))
    dbCon.commit() # commit the changes to the database, permanently adding the song to the table
    print(f"{songTitle} added to the database at SongID {dbCursor.lastrowid}")

"""
The `if __name__ == "__main__":` statement is used to check if 
the current script is being run directly or if it is being imported as a module.
"""
if __name__ == "__main__":
    insert_data()


# Add songs to the songs table (Manual Method)
# dbCursor.execute("INSERT INTO songs (Title, Artist, Genre) VALUES ('The Box', 'Roddy Ricch', 'Hip-Hop')")
# dbCursor.execute("INSERT INTO songs (Title, Artist, Genre) VALUES ('Don't Start Now', 'Dua Lipa', 'Pop')")
# dbCursor.execute("INSERT INTO songs (Title, Artist, Genre) VALUES ('Circles', 'Post Malone', 'Pop')")
# dbCursor.execute("INSERT INTO songs (Title, Artist, Genre) VALUES ('Life Is Good', 'Future ft. Drake', 'Hip-Hop')")
# dbCursor.execute("INSERT INTO songs (Title, Artist, Genre) VALUES ('Memories', 'Maroon 5', 'Pop')")
# dbCursor.execute("INSERT INTO songs (Title, Artist, Genre) VALUES ('Someone You Loved', 'Lewis Capaldi', 'Pop')")
# dbCursor.execute("INSERT INTO songs (Title, Artist, Genre) VALUES ('Dance Monkey', 'Tones and I', 'Pop')")
# dbCon.commit() # commit the changes to the database
