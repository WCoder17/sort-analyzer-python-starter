# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
print(randomData[0:50])
print(reversedData[0:50])
print(nearlySortedData[0:50])
print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
def insertionSort(arr):
    n = len(arr)
    if n <= 1:
        return  
    for i in range(1, n):  
        j = arr[i]  
        x = i-1
        while x >= 0 and j < arr[x]:  
            arr[x+1] = arr[x]  
            x -= 1
        arr[x+1] = j 
  


startTime = time.time()
insertionSort(fewUniqueData)
endTime = time.time()
print(f"Selection Sort Random Data: {endTime - startTime} seconds")

# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")
