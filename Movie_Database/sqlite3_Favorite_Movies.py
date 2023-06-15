#Database of favorite movies

import sqlite3

#Establish connection to working database
Connection = sqlite3.connect("Favorite_Movies.db")

#Create cursor to traverse working database
Cursor = Connection.cursor()

#Create primary table for database
#Cursor.execute("CREATE TABLE Movies(Title, Year, Actor)")

#Create list of information
Movie_List_Data = [

    ("Training Day", 2001, "Denzel Washington"),
    ("Justice League", 2013, "Flash"),
    ("Tom Clancy's Without Remorse", 2021, "Michael B. Jordan"),
    ("Se7en", 1995, "Brad Pitt"),
    ("The Departed", 2006,"Jack Nicholson"),
    ("The Wolf of Wall Street", 2013, "Leonardo DiCaprio"),
    ("Catch Me If You Can", 2002, "Leonardo DiCaprio"),
    ("Superbad", 2007, "Jonah Hill"),
    ("21 Jump Street", 2012, "Channing Tatum"),
    ("Scott Pilgrim vs. the World", 2010 ,"Michael Cera"),
    ("Kate", 2021, "Mary Elizabeth Winstead"),
    ("Surf's Up", 2007, "Shia LaBeouf"),
    ("Disturbia", 2007, "Shia LeBeouf"),
    ("Lawless", 2012, "Shia LeBeouf"),
    ("Fury", 2014, "Brad Pitt"),
    ("Inglourious Bastards", 2009, "Brad Pitt"),
    ("Fight Club", 1999, "Brad Pitt"),
    ("Casino Royale", 2006, "Daniel Craig"),
    ("The Girl with the Dragon Tattoo", 2011, "Daniel Craig"),
    ("Defiance", 2008, "Daniel Craig"),
    ("Rogue One: A Star Wars Story", 2016, "Diego Luna"),
    ("Imperium", 2016, "Daniel Radcliffe"),
    ("Hangover", 2009, "Bradley Cooper"),
    ("Silver Linings Playbook", 2012, "Jennifer Lawrence"),
    ("Zero Dark Thirty", 2012, "Jessica Chastain"),
    ("Joker", 2019, "Joaquin Phoenix"),
    ("The Intern", 2015, "Robert De Niro"),
    ("John Wick", 2014, "Keanu Reeves"),
    ("Schindler's List", 1993, "Liam Neeson"),
    ("Spider-Man: Into the Spider-Verse", 2018, "Shameik Moore"),
    ("Scarface", 1983, "Al Pacino"),
    ("American Gangster", 2007, "Denzel Washington"),
    ("Spider-Man: Across the Spider-Verse", 2023, "Shameik Moore"),
    ("Spider-Man: No Way Home", 2021, "Tom Holland"),
    ("Harry Potter and the Deathly Hallow: Part 2", 2011, "Daniel Radcliffe"),
    ("Gone Girl", 2014, "Ben Affleck"),
    ("Beirut", 2018, "Rosamund Pike"),
    ("Live by Night", 2016, "Ben Affleck"),
    ("The Roads Not Taken", 2020, "Elle Fanning"),
    ("Astro Boy", 2009, "Nicholas Cage"),
    ("Ashby", 2015, "Emma Roberts")
]

#Verify table existence
def Verify_Table(Target_Table):
    SQL_Query = f"SELECT name FROM sqlite_master WHERE name='{Target_Table}'"
    Results = Cursor.execute(SQL_Query)
    if Results.fetchone is None:
        print("Table does not exist")
        return False
    else:
        print("Table does exist")
        return True

Verify_Table("Movies")
