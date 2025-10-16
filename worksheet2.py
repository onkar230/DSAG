"""
 1. Implement Selection Sort:
Recall that in each iteration, Selection Sort finds the minimum or maximum in the
unsorted part of the array and moves it to the sorted part. Repeat until the array is
fully sorted ###
"""
from random import sample



class Iteration:
    def __init__(self):
        self.data = []
        self.max_size = 100
       
    def initialise(self):
        self.data = sample(range(1, 3 * self.max_size), self.max_size)
        
    def printAll(self):
        print("The size of the random array" + str(len(self.data)))
        print("Before sorting, the array is" + str(self.data))
        
    def selectionSort(self):
        for i in range(len(self.data) - 1):
            indMin = i 
            for j in range(i + 1, len(self.data)):
                # find the index of smallest item in the unsorted part of the list
                if self.data[j] < self.data[indMin]:
                    indMin = j
            # index of smallest located, move item to position i, swap data[i]
            self.data[indMin], self.data[i] = self.data[i], self.data[indMin]
        return self.data

    def insertionSort(self):
        for i in range(1, len(self.data)):
            current = self.data[i]
            j = i
            while j > 0 and current < self.data[j - 1]:
                self.data[j] = self.data[j - 1]
                j -= 1
            self.data[j] = current
        return self.data


    def bubbleSort(self):
        for i in range(len(self.data) -1):
            for j in range(len(self.data) -1):
                if (self.data[j] > self.data[j + 1]):
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
        return self.data
    


    def linearSearch(self, item):
        for ind in range(len(self.data)):
            if(self.data[ind] == item):
                return ind
        print("Item not found")
        return -1





    def binaryiterSearch(self, item):
        start = 0
        end = len(self.data) - 1
        while (start <= end):
            mid = (start + end) // 2
            if (self.data[mid] < item):
                start = mid + 1
            elif (self.data[mid] > item):
                end = mid - 1
            else:
                return mid
        print("Item not found")
        return -1



    



    def binaryRecurSearch(self, item):
        return self._binaryRecurSearchHelper(self.data, 0, len(self.data) - 1, item)

    def _binaryRecurSearchHelper(self, arr, start, end, item):
        # arr has to be sorted array
        if start <= end:
            mid = (start + end) // 2
            if arr[mid] < item:
                return self._binaryRecurSearchHelper(arr, mid + 1, end, item)
            elif arr[mid] > item:
                return self._binaryRecurSearchHelper(arr, start, mid - 1, item)
            else:
                return mid
        print("Item not found")
        return -1







arr = Iteration()
arr.initialise()
arr.printAll()
print("After sorting, the array is" + str(arr.selectionSort()))


"""
2. Implement Insertion Sort:
Recall that in each iteration, Insertion Sort takes an element from the unsorted part,
finds its correct position in the sorted part, and inserts it. Repeat until the array is fully
sorted.
"""

arr.initialise()
arr.printAll()
print("After the insertion sort, the array is " + str(arr.insertionSort()))


"""
3. Implement Bubble Sort:
Recall that in each iteration, Bubble Sort compares adjacent elements in the unsorted
part and swaps them if needed. After each pass, the last element of the unsorted part
is in its final position. Repeat until the array is fully sorted."""
""""""

arr.initialise()
arr.printAll()
print("After the bubble sort, the array is " + str(arr.bubbleSort()))


"""
4. Implement Linear Search for an Array or List, sequentially checking
each element of the array or list to find a target value.

"""
arr.initialise()
arr.printAll()
ind = arr.linearSearch(5)
print(ind)
print("After the insertion sort, the array is " + str(arr.insertionSort()))
ind = arr.linearSearch(5)
print(ind)



"""
5. Implement Binary Search for a Sorted Array (Iterative Method), halving
the search space at each step to efficiently locate a target value.
"""


arr.initialise()
arr.printAll()
print("After the bubble sort, the array is " + str(arr.bubbleSort()))
ind = arr.linearSearch(5)
print(ind)
ind = arr.binaryiterSearch(5)
print(ind)



"""
6. Implement Binary Search for a Sorted Array (Recursive Method) and
compare its performance with the iterative method in Ex 5 using arbitrary
sorted arrays.

"""

arr.initialise()
arr.printAll()
print("After the bubble sort, the array is " + str(arr.bubbleSort()))  
ind = arr.binaryiterSearch(5)
print(ind)
ind = arr.binaryRecurSearch(5)
print(ind)