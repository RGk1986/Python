from connect import * # import the connect.py module 
dbCursor.execute(""" 
CREATE TABLE "members" (
	"MemberID"	INTEGER NOT NULL UNIQUE,
	"Firstname"	TEXT,
	"Lastname"	TEXT,
	"Email"	TEXT,
	PRIMARY KEY("MemberID" AUTOINCREMENT)
)""")

# ...............................
dbCursor.execute("""
CREATE TABLE "songs" (
	"SongID"	INTEGER NOT NULL UNIQUE,
	"Title"	TEXT,
	"Artist"	TEXT,
	"Genre"	TEXT,
	PRIMARY KEY("SongID" AUTOINCREMENT)
)""")
# ......... Create the table(s) with the foreign keys last..................
dbCursor.execute("""
  CREATE TABLE "downloads" (
	"DownID"	INTEGER NOT NULL UNIQUE,
	"SongID"	INTEGER,
	"MemberID"	INTEGER,
	"Date"	TEXT,
	PRIMARY KEY("DownID" AUTOINCREMENT),
	FOREIGN KEY("SongID") REFERENCES "songs"("SongID"),
	FOREIGN KEY("MemberID") REFERENCES "members"("MemberID")
)""")

