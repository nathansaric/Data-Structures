# Nathan Saric - 02/04/2021

# Question 2.3: WebpagePriorityQueue

from WebPageIndex import *
import re # Used to properly format and remove punctuation from strings

# WebpagePriorityQueue class containing an initialization function and 7 functions 
# that fulfill the requirements set out in Question 2.3
class WebpagePriorityQueue:
    
    # Initialization function for WebpagePriorityQueue class
    def __init__(self, query, webpageSet):
        self.query = query
        self.webpages = webpageSet
        self.webpageHeap = self.createMaxHeap()

    # createMaxHeap function that creates the corresponding MaxHeap for a given set of WebPageIndex instances
    # The priority of a WebPageIndex instance is the sum of the frequencies of the words for a given query
    def createMaxHeap(self):
        webpageHeap = []
        for webpage in self.webpages:
            priorityLevel = self.getPriority(webpage)
            newWebPage = [priorityLevel, webpage, webpage.fileName]
            # Append the new WebPageIndex instance then call the heapUp function to properly reorder the webpageHeap
            webpageHeap.append(newWebPage)
            self.heapUp(webpageHeap, len(webpageHeap) - 1)
        return webpageHeap

    # getPriority function that returns the priority level of a given webPage 
    # Each query is lowercase and stripped of any punctuation using a regular expression
    def getPriority(self, webpage):
        queryList = self.query.lower()
        queryList = re.sub(r'[^\w\s]', '', queryList).split()

        priorityLevel = 0
        for query in queryList:
            priorityLevel += webpage.getCount(query)
        
        return priorityLevel
            
    # peek function that returns the WebPageIndex instance with the highest priority from webpageHeap
    def peek(self):
        if len(self.webpageHeap) == 0:
            highestPriority = None
        else:
            highestPriority = self.webpageHeap[0]

        return highestPriority

    # poll function that removes and returns the WebPageIndex instance with the highest priority from webpageHeap
    def poll(self):
        if len(self.webpageHeap) == 0:
            highestPriority = None
        else:
            highestPriority = self.webpageHeap[0]
            self.webpageHeap[0] = self.webpageHeap[-1]
            # Pop the WebPageIndex instance then call the heapDown function to properly reorder the webpageHeap
            self.webpageHeap.pop()
            self.heapDown(self.webpageHeap, 0)

        return highestPriority

    # heapUp function that properly reorders the webpageHeap by starting at the last element in the heap
    def heapUp(self, heap, index):
        parentIndex = (index - 1)// 2
        if parentIndex < 0:
            return

        if heap[parentIndex][0] < heap[index][0]:
            # Swap values in a bubble sort fashion
            temp = heap[parentIndex]
            heap[parentIndex] = heap[index]
            heap[index] = temp
            # Recursively call the function with the parent index
            self.heapUp(heap, parentIndex)

    # heapDown function that properly reorders the webpageHeap by starting at the first element in the heap
    def heapDown(self, heap, index):
        childIndex = (2 * index) + 1
        if childIndex >= len(heap):
            return

        if childIndex + 1 < len(heap) and heap[childIndex][0] < heap[childIndex + 1][0]:
            childIndex += 1
        if heap[index][0] < heap[childIndex][0]:      
            # Swap values in a bubble sort fashion
            temp = heap[index]
            heap[index] = heap[childIndex]
            heap[childIndex] = temp
            # Recursively call the function with the child index 
            self.heapDown(heap, childIndex)

    # reheap function that accepts a new query and reheaps the webpageHeap accordingly
    def reheap(self, query):
        if query != self.query:
            self.webpageHeap = self.creatMaxHeap()
            self.query = query
        else: 
            return
