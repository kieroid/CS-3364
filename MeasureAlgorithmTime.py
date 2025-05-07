from QuickHybridSort import *

def quickSort(array, low, high):
    if low < high:
        partitionInt = partition(array, low, high)
        quickSort(array, low, partitionInt - 1)
        quickSort(array, partitionInt + 1, high)

newTestArray = [];
for i in range(5):
    #newTestArray = [5,4,3,2,1];
    for num in range(50):
        #newTestArray.append(randint(100,998));
        newTestArray.append(num);


    startTime = time.time();
    #a = insertionSort(newTestArray);
    #a = quickSort(newTestArray,0,len(newTestArray) - 1);
    a = QuickHybridSort(newTestArray, 20);
    print(time.time() - startTime);


