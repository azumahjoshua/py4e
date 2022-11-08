import sqlite3

conn = sqlite3.connect('music.sqlite')
# A cursor is like a file handle that we can use to perform operations on the data stored in the database is very similar conceptually to calling open() when dealing with text files.
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

cur.close()
