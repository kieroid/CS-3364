from random import randint
from QuickHybridSort import *

def quickHybridSortTest(K):
    testArray = [];
    for num in range(20):
        testArray.append(randint(10,98))
    
    if(QuickHybridSort(testArray,K) == sorted(testArray)):
        print(testArray, "- Passed!");
        return(0);
    else:
        print(testArray, "- Failed!");
        return(1);

a = 0;
for i in range(20):
    print("Testing for K =", i);
    for j in range(10):
        a += quickHybridSortTest(i);
    if(a == 0):
        print("Success for all K values!");



