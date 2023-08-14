from connect import *
import requests

# Replace with your actual TMDb API key
API_KEY = "b99b4073fd2ce0958b7052b77938136b"

# Fetch movie data from TMDb API
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=en-US&page=1"
response = requests.get(url)
data = response.json()

# Insert movie data into the tblFilms table
for movie in data["results"]:
    title = movie["title"]
    yearReleased = movie["release_date"][:4]
    rating = str(movie["vote_average"])
    duration = "N/A"  # TMDb API doesn't provide exact duration
    genre = "N/A"  # TMDb API doesn't provide exact genre

    dbCursor.execute("""
        INSERT INTO tblFilms (title, yearReleased, rating, duration, genre)
        VALUES (?, ?, ?, ?, ?)
    """, (title, yearReleased, rating, duration, genre))

# Commit changes and close the connection
dbCon.commit()
dbCon.close()
