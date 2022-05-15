# Nathan Saric - 01/29/2021

# Question 3: Binary Search or Linear Search?

import random
import timeit

# A linear search function that returns True if the target 
# is in the search list or returns False otherwise. 
def linearSearch(searchList, target):
    for i in range(len(searchList)):
        if (searchList[i] == target):
            return True # target is found 
    return False # target is not found

# A binary search function that returns True if the target
# is in the search list or returns False otherwise. 
def binarySearch(searchList, target):
    startIndex = 0
    endIndex = len(searchList) - 1

    while startIndex <= endIndex:
        midpoint = startIndex + (endIndex - startIndex) // 2
        midpointIndex = searchList[midpoint]

        if midpointIndex == target: # target is equal to the midpoint value
            return True # target is found

        elif target < midpointIndex: #target is in first half of the search list
            endIndex = midpoint - 1

        else: # target is in the second half of the search list 
            startIndex = midpoint + 1
    return False # target is not found

# A helper function used in mergeSort to merge two lists in ascending order
def merge(leftHalf, rightHalf):
    sortedList = []
    leftIndex = 0
    rightIndex = 0 

    while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
        if leftHalf[leftIndex] < rightHalf[rightIndex]:
            sortedList.append(leftHalf[leftIndex]) # appends value from the left list to the sorted list
            leftIndex+= 1
        
        else:
            sortedList.append(rightHalf[rightIndex]) # appends value from the right list to the seorted list
            rightIndex+= 1
    
    sortedList.extend(leftHalf[leftIndex:]) # extends all values in the left list to the sorted list
    sortedList.extend(rightHalf[rightIndex:]) # extends all values in the right list to the sorted list
    return sortedList # returns a list sorted in ascending order

# A merge sort function that sorts and returns a list in ascending order
def mergeSort(searchList):
    if len(searchList) <= 1:
        return searchList # no need to sort an array with 0 or 1 elements

    midpoint = len(searchList) // 2
    leftHalf = mergeSort(searchList[:midpoint])
    rightHalf = mergeSort(searchList[midpoint:])
    return merge(leftHalf, rightHalf) # calls a helper function used to merge arrays

# A function that creates a list and search list using a pseudo-random number generator
def randomList(n, k):
    random.seed(k) # a seed that ensures the same random numbers are generated for both algorithms
    S = random.sample(range(2, (n*n), 2), n) # random list with only even integer values

    kFirstHalf = random.sample(S, (k//2)) # random search list with only even integer values
    kSecondHalf = random.sample(range(1, (n*n), 2), (k//2)) # random search list with only odd integer values
    k = kFirstHalf + kSecondHalf
    return S, k

# An implementation of Algorithm A using linearSearch to search for all k values in S
def algorithmA(n, k):
    S, k = randomList(n, k)

    for i in k: 
        linearSearch(S, i)

# An implementation of Algorithm B using binarySearch to search for all k values in S
# The algorithm first calls mergeSort to initially sort the search list in ascending order
def algorithmB(n, k):
    S, k = randomList(n, k)
    sortedList = mergeSort(S)
    
    for i in k: 
        binarySearch(S, i)
    
# A timer function that uses the timeit module to calculate the execution time of Algorithm A and B
def timer(n, k):
    startATime = timeit.default_timer()
    algorithmA(n, k)
    endATime = timeit.default_timer()
    algorithmATime = endATime - startATime

    startBTime = timeit.default_timer()
    algorithmB(n, k)
    endBTime = timeit.default_timer()
    algorithmBTime = endBTime - startBTime

    return(algorithmATime, algorithmBTime)

# The test function used to conduct the experiment and prints the 
# corresponding algorithm times and minumum k value 
def test(n, k):
    print('-' * 40)
    print('Testing n = ' + str(n))
    while True:
        algorithmATime, algorithmBTime = timer(n, k)
        k += 1 # increments the length of the search list by 1 each iteration

        if (algorithmATime > algorithmBTime): # breaks the loop if Algorithm B is faster than Algorithm A
            print("Algorithm A time: " + str(algorithmATime))
            print("Algorithm B time: " + str(algorithmBTime))
            print("Minimum k value: " + str(k))
            break

# The main function used to initialize the values for n and k, 
# and then proceed with the testing
def main():
    n = [1000, 5000, 10000]
    k = 10

    for i in range(len(n)):
        test(n[i], k)

if __name__ == "__main__":
    main()
