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

# Task 1 will begin here.
#########################

#insertion sort

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

#partitioning

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

#recursivehelper

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

#quickhybridsort

def QuickHybridSort(array, K):
    arrayCopy = array.copy();
    #...
    recursiveHelper(arrayCopy, 0, len(arrayCopy) - 1, K);
    #...
    return arrayCopy;
