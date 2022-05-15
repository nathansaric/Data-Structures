# Nathan Saric - 02/04/2021

# Question 2.4: Process Queries

#from AVLTreeMap import *
#from WebPageIndex import *
from WebpagePriorityQueue import *
import os # used to read filenames from a given folder path

# ProcessQueries class containing an initialization function, 3 functions, 
# and the main function that fulfill the requirements set out in Question 2.4 
class ProcessQueries:

    # Initialization function for ProcessQueries class
    def __init__(self, folderPath, queryPath):
        self.fileList = []
        self.files = self.readFiles(folderPath)
        self.queryList = self.readQueries(queryPath)
        self.userLimit = self.getUserLimit()

    # readFiles function that accepts a folder path and returns a list of WebPageIndex instances
    # The list represents the files in the given input folder
    def readFiles(self, folderPath):
        files = []
        # os.listdir() returns a list containing the names of all files in the directory
        for file in os.listdir(folderPath):
            # os.path.join() joins pathname components into a single pathname
            self.fileList.append(os.path.join(folderPath, file))

        for fileName in self.fileList:
            # Creating a WebPageIndex instance for each webpage in the folder
            webPage = WebPageIndex(fileName)
            files.append(webPage)

        return files

    # readQueries function that accepts a query path and returns a list of all queries 
    def readQueries(self, queryPath):
        queryFile = open(queryPath, 'r').read().lower().splitlines()
        return queryFile

    # getUserLimit function that prompts the user for a positive integer in a robust manner
    # The user limit determines how many search results will be displayed
    def getUserLimit(self):    
        inputFlag = False
        while not inputFlag:
            try:
                userLimit = input("Enter the number of results to display: ")
                userInput = int(userLimit)
                if userInput <= 0:
                    print("Number must be greater than 0. Please try again.")
                else:
                    inputFlag = True
            except ValueError:
                print("Invalid input. Please try again.")
        
        return userLimit

# main function that initializes a folder path and a query path and then prints out the file names 
# from best to worst match given a query 
def main():
    # These paths are local to my computer and will need to be modified when testing on another computer
    folderPath = '/Users/nathan/Documents/queens/CISC235/ASSIGNMENT 2/dataset'
    queryPath = '/Users/nathan/Documents/queens/CISC235/ASSIGNMENT 2/queries.txt'

    PQ = ProcessQueries(folderPath, queryPath)
    queries = PQ.queryList
    webpages = PQ.files
    userLimit = int(PQ.userLimit)

    for query in queries:
        print('-' * 50)
        print("Query: " + str(query))
        searchEngine = WebpagePriorityQueue(query, webpages)
        displayLimit = min(userLimit, len(searchEngine.webpageHeap))

        for i in range(displayLimit):
            searchResult = searchEngine.poll()
            if searchResult[0] != 0:
                print("Priority Rating: " + str(searchResult[0]) +  " | " +
                      "File Name: " + str(searchResult[2]))

if __name__ == '__main__':
    main()
