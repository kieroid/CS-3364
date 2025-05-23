"""
Part 1.
Create a sorting algorithm QuickHybridSort(A[n], K) with two inputs:
- A[n]: A numerical array of length n.
- K: A threshold value. If a subarray has length ≤ K, it should be sorted using Insertion Sort. Otherwise, Quicksort is used.

    Task 1.
    - Implement QuickHybridSort, providing your own InsertionSort and Partition methods for Quicksort.
    - Test correctness by comparing results to your language’s built-in sort.
    - Include source code and correctness verification. 

    Task 2.
    - Measure average run times for various n and K. 
    - Use random arrays. 
    - Plot performance for at least 5 different n values while varying K.
    - Plot showing average run time vs K, with multiple curves for different n.

    Task 3.
    - Compare QuickHybridSort to both Quicksort and Insertion Sort.
    - Identify and explain the optimal K value(s).
    - Plot optimal K vs n, and a comparison plot showing performance of all three algorithms. 
    - Provide an explanation.

    Task 4.
    - Repeat Tasks 2 and 3 using pre-sorted input. How do results differ? Why?
    - Include observations and explanations for sorted input tests.
"""
import time
from random import randint

timePerK = [];

# Task 1 will begin here.
#########################

# insertionSort (self explained. its an insertion sort algorithm)

def insertionSort(array):
    #print("Sorting:", array);
    arrayLength = len(array);

    if arrayLength <= 1:
        return array;

    for currentNum in range(1, arrayLength):
        storedElement = array[currentNum];
        previousNum = currentNum - 1;
        while(previousNum >= 0 and storedElement < array[previousNum]):
            array[previousNum + 1] = array[previousNum];
            previousNum -= 1;
        array[previousNum + 1] = storedElement;
    return array;

# partition (splits up the array into a smaller piece)

def partition(array, low, high):
    #print("Partitioning:",array);
    pivot = array[high];
    i = low - 1;

    for j in range(low, high):
        if(array[j] <= pivot):
            i += 1;
            array[i], array[j] = array[j], array[i];
    array[i + 1], array[high] = array[high], array[i + 1];
    return i + 1;

# recursiveHelper (called by QuickHybridSort)

def recursiveHelper(array, low, high, K):
    if(low < high):
        if(high - low + 1 <= K):
            subArrayCopy = array[low:high + 1]; # get the partition of the array
            insertionSort(subArrayCopy);
            array[low:high + 1] = subArrayCopy;
        else:
            pivot = partition(array, low, high);
            recursiveHelper(array, low, pivot - 1, K);
            recursiveHelper(array, pivot + 1, high, K);

# QuickHybridSort function

def QuickHybridSort(array, K):
    arrayCopy = array.copy();
    #...
    recursiveHelper(arrayCopy, 0, len(arrayCopy) - 1, K);
    #...
    return arrayCopy;


# quickHybridSortTest (for verification)

def quickHybridSortTest(K,totalKTested):
    testArray = [];
    for i in range(totalKTested):
        testArray.append(i);

    #for num in range(totalKTested):
    #    testArray.append(randint(100,998))
    
    if(QuickHybridSort(testArray,K) == sorted(testArray)):
        #print(testArray, "- Passed!");
        return(0);
    else:
        #print(testArray, "- Failed!");
        return(1);

# verifySortAlgorithm (checks if all tests passed)

def verifySortAlgorithm(numPerK = 8, totalKTested = 25):
    a = 0;
    for i in range(1,totalKTested + 1):
        #print("Testing for K =", i);
        for _ in range(numPerK):
            startTime = time.time();
            a += quickHybridSortTest(i,totalKTested);
            timePerK.append([time.time() - startTime,i]);
        #if(a == 0):
        #    print("Success for all K values!");
    return(a);

# uncomment below to get working

#errors = verifySortAlgorithm();
#for i in range(len(timePerK)):
#    print(str(timePerK[i][0]) + ", " + str(timePerK[i][1]));

#print(f"{'\033[1m'}Test data ended. Checking for errors...")
#print(f"{'\033[91m'}TOTAL ERRORS:", errors)

