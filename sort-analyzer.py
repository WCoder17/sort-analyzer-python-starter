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
def selectionSort(arr, n):

    for i in range (n):
        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j
        
        (arr[i], arr[min_index]) = (arr[min_index], arr[i])

n = len(fewUniqueData)
startTime = time.time()
selectionSort(fewUniqueData, n)
endTime = time.time()
print(f"Selection Sort Random Data: {endTime - startTime} seconds")

# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")
