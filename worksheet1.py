



class Queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = -1
        self.max_size = 15
        
        
    def enequeue(self, NewData):
        print("Enqueueing " + str(NewData))
        if self.tail == self.max_size - 1:
            print("Queue is full")
            raise OverflowError("Cannot insert inro a full queue")
        self.tail += 1
        self.data.insert(self.tail, NewData)
        print("Now the tail is at " + str(self.tail))
        
    def dequeue(self):
        if
        jkdiosjfdlkks
        fdgadsdfgdfg