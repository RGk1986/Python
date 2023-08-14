from connect import *

def insertManySongs():
    songList = [
    # ("Shape of You", "Ed Sheeran", "Pop"),
    # ("Bohemian Rhapsody", "Queen", "Rock"),
    # ("Uptown Funk", "Mark Ronson ft. Bruno Mars", "Funk"),
    # ("Rolling in the Deep", "Adele", "Pop"),
    # ("Billie Jean", "Michael Jackson", "Pop"),
    # ("Hotel California", "Eagles", "Rock"),
    # ("Old Town Road", "Lil Nas X", "Hip-Hop"),
    # ("Happy", "Pharrell Williams", "Pop"),
    # ("Thinking Out Loud", "Ed Sheeran", "Pop"),
    # ("Imagine", "John Lennon", "Rock")
    # ("Für Elise", "Ludwig van Beethoven", "Classical"),
    # ("Canon in D", "Johann Pachelbel", "Baroque"),
    # ("Symphony No. 9 'From the New World'", "Antonín Dvořák", "Romantic"),
    # ("Clair de Lune", "Claude Debussy", "Impressionist"),
    # ("The Four Seasons - Spring", "Antonio Vivaldi", "Baroque"),
    # ("Moonlight Sonata", "Ludwig van Beethoven", "Classical"),
    # ("Ride of the Valkyries", "Richard Wagner", "Romantic"),
    # ("Ave Maria", "Franz Schubert", "Romantic"),
    # ("Swan Lake", "Pyotr Ilyich Tchaikovsky", "Romantic"),
    # ("Carmen - Habanera", "Georges Bizet", "Opera")
    ]
    
    # insert all songs in the list of tuples into the songs table
    dbCursor.executemany("INSERT INTO songs VALUES (NULL, ?, ?, ?)", songList)
    dbCon.commit() # commit the changes to the database
    
if __name__ == '__main__':
    insertManySongs()
    print(f"Songs added to the database at SongID {dbCursor.lastrowid}")
        