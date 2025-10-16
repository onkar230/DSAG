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




arr = Iteration()
arr.initialise()
arr.printAll()
print("After sorting, the array is" + str(arr.selectionSort()))