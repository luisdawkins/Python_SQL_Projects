#Import module necessary to interact with SQL code using python
import sqlite3

#Establishes a connection to working database
#If a database has not been created it will do so
Connection = sqlite3.connect("GTA.db")

#Interacting with database requires cursor
Cursor = Connection.cursor()

# 'Cursor' is used to execute SQL commands in working database
Cursor.execute("create table gta (Release_Year integar, Release_Name text, City text)")

#This is our example data
release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

#This command is used to run multiple commands
Cursor.executemany("insert into gta values (?,?,?)", release_list)

#Print Database rows
for row in Cursor.execute("select * from gta"):
    print(row)

#Print specific rows
print("********************")
#Similar to a fstring in python the dictionary key of c is a variable for "Liberty City"
Cursor.execute("select * from gta where City=:c", {"c": "Liberty City"})
#The fetchall() command returns query results as a list
Gta_Search = Cursor.fetchall()
print(Gta_Search)

#Create new table for multi-table manipulation
Cursor.execute("create table Cities (Gta_City text, Real_City text)")
Cursor.execute("insert into Cities values (?,?)", ("Liberty City", "New York"))
Cursor.execute("select * from Cities where Gta_City=:c", {"c": "Liberty City"})
Cities_Search = Cursor.fetchall()
print(Cities_Search)

#Manipulate database data
print("****************************")
for i in Gta_Search:
    adjusted = [Cities_Search[0][1] if value == Cities_Search[0][0] else value for value in i]
    print(adjusted)

#Closes connection to working database
Connection.close()
