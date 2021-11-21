import pandas as pd
dataFile = "HomeLibrary.txt"
class HomeLibrary():
    books = []
    def __init__(self,name,author,genre,year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

print(HomeLibrary)
print("This library welcomes you")
while True:
    print("0. Exit\n1. Search for book")
    userInput = str(input())
    if input == "0":
        break
    elif userInput == "1":
        print("Enter keyword to search\n")
        keyword1 = str(input)
        file = open(dataFile, "r+").readlines()
        for line in file:
            HomeLibrary

        for book1 in "HomeLibrary.txt":
            if keyword1 in book1:
                print(book1)

       
else:
    print("Incorrect input\n")
input()
    



