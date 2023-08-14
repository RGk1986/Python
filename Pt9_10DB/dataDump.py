from connect import *

# Create a function to dump data into the songs table

def dataDump():
    # Load the songs.sql (script file)
    with open(r'Pt9_10DB\songs.sql') as sqlScript:
        dumpData = sqlScript.read()
        dbCursor.executescript(dumpData)
        dbCon.commit()

if __name__ == '__main__':
    dataDump()
    print('Data dumped successfully')
