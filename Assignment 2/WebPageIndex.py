# Nathan Saric - 02/04/2021

# Question 2.2: WebPageIndex

from AVLTreeMap import *
import re # Used to properly format and remove punctuation from strings

# WebPageIndex class containing an initialization function and 3 functions 
# that fulfill the requirements set out in Question 2.2
class WebPageIndex:

    # Initialization function for WebPageIndex class
    def __init__(self, file):
        self.fileName = file
        self.AVLTreeMap = self.createAVLTreeMap()
        self.webpagePriority = 0

    # createAVLTreeMap function that creates the corresponding AVLTree for a given file 
    # Each key refers to a word in the file and each value represents a list containing all indices of the word in the file
    def createAVLTreeMap(self):
        AVLTree = AVLTreeMap()
        wordsList = self.openFile()
        
        # Creating a dictionary to store the key-value pairs
        dictPositions = {}

        for word in range(len(wordsList)):
            if wordsList[word] not in dictPositions:
                # Add a new word as a key in the dictionary
                dictPositions[wordsList[word]] = [word]
            else:
                # A the index of a word as a value in the dictionary
                dictPositions[wordsList[word]].append(word)

        # Building an AVLTree and inserting each key-value pair into the AVLTree
        for pair in dictPositions:
            AVLTree.put(pair, dictPositions[pair])
        
        return AVLTree

    # openFile function that opens and reads a file and returns a list of all words in the file
    # Each item in the list is lowercase and stripped of any punctuation using a regular expression
    def openFile(self):
        readfile = open(self.fileName, 'r')
        stringFile = readfile.read().lower()
        stringFile = re.sub(r'[^\w\s]', '', stringFile).split()
        readfile.close()
        return stringFile

    # getCount function that returns the number of times a given word appears on a WebPage
    def getCount(self, s):
        if self.AVLTreeMap.get(s) == None:
            count = 0
        else:
            count = len(self.AVLTreeMap.get(s))

        return count

# Test code
if __name__ == '__main__': 

    # This testFile is local to my computer and will need to be modified when testing on another computer
    testFile = '/Users/nathan/Documents/queens/CISC235/ASSIGNMENT 2/dataset/doc1-arraylist.txt'
    AVLTree = WebPageIndex(testFile)
    root = AVLTree.AVLTreeMap.rootNode

    # This will print the words out in alphabetical order
    print("In-Order Traversal of Tree: " + str(AVLTree.AVLTreeMap.inorderTraversal(root)))
