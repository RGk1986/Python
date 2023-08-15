from connect import *

# The code `dbCursor.execute` is used to execute a SQL query on the database. In this case, it is
# executing a query to create a table named "tblFilms" with the specified columns: "filmID" (an
# auto-incrementing integer and primary key), "title" (text), "yearReleased" (integer), "rating"
# (integer), "duration" (integer), and "genre" (text).
dbCursor.execute("""
CREATE table "tblFilms" (
"filmID" INTEGER UNIQUE,
"title" TEXT,
"yearReleased" INTEGER,
"rating" INTEGER,
"duration" INTEGER,
"genre" TEXT,
PRIMARY KEY("filmID" AUTOINCREMENT)
)""")

