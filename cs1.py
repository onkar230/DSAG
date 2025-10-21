# ---------------- STACK ----------------
class Stack:
    def __init__(self, max_size=10):
        # data = where items are stored
        # top = index of the top item (-1 means empty)
        # max_size = how many items can fit
        self.data, self.top, self.max_size = [], -1, max_size

    def push(self, item):  # Add an item on top
        if self.top == self.max_size - 1: raise OverflowError
        self.top += 1
        self.data.insert(self.top, item)

    def pop(self):  # Remove the item from the top
        if self.top == -1: raise IndexError
        item = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        return item

    def peek(self):  # Look at the top item (don’t remove it)
        if self.top == -1: raise IndexError
        return self.data[self.top]

    def length(self):  # Return how many items in stack
        return self.top + 1


# ---------------- QUEUE ----------------
class Queue:
    def __init__(self, max_size=10):
        # data = where items are stored
        # head = index of the front
        # tail = index of the back
        self.data, self.head, self.tail, self.max_size = [], 0, -1, max_size

    def enqueue(self, item):  # Add item to the back
        if self.tail == self.max_size - 1: raise OverflowError
        self.tail += 1
        self.data.insert(self.tail, item)

    def dequeue(self):  # Remove item from the front
        if self.tail == -1: raise IndexError
        item = self.data[self.head]
        # Shift all items forward
        for i in range(self.head, self.tail):
            self.data[i] = self.data[i+1]
        del self.data[self.tail]
        self.tail -= 1
        return item

    def peek(self):  # Look at the front item
        if self.tail == -1: raise IndexError
        return self.data[self.head]

    def length(self):  # Return how many items in queue
        return self.tail + 1


# ---------------- CIRCULAR QUEUE ----------------
class CircularQueue:
    def __init__(self, max_size=5):
        # fixed size list with None
        self.data, self.head, self.tail, self.max_size = [None]*max_size, 0, 0, max_size

    def isEmpty(self):  # True if no items
        return self.head == self.tail

    def isFull(self):  # True if queue filled up
        return (self.tail - self.head == self.max_size)

    def enqueue(self, item):  # Add item at tail
        if self.isFull(): raise OverflowError
        self.data[self.tail % self.max_size] = item  # wrap around with %
        self.tail += 1

    def dequeue(self):  # Remove item at head
        if self.isEmpty(): raise IndexError
        item = self.data[self.head % self.max_size]
        self.head += 1
        return item


# ---------------- ALGORITHMS ----------------
def reverse_queue(q):
    # Put all items into stack, then back into queue (reverses order)
    s = Stack()
    while q.length() > 0:
        s.push(q.dequeue())
    while s.length() > 0:
        q.enqueue(s.pop())


def remove_adjacent(s):
    # Remove letters that are next to each other and the same
    stack = Stack()
    for ch in s:
        if stack.length() > 0 and stack.peek() == ch:
            stack.pop()  # remove if duplicate next to it
        else:
            stack.push(ch)  # keep if different
    return "".join(stack.data[:stack.length()])


def bracket_check(expr):
    # Check if all brackets are matched properly
    pairs, stack = {')':'(', ']':'[', '}':'{'}, Stack()
    for ch in expr:
        if ch in pairs.values():  # opening bracket
            stack.push(ch)
        elif ch in pairs:  # closing bracket
            if stack.length()==0 or stack.pop()!=pairs[ch]:
                return False
    return stack.length() == 0  # must be empty at end


# ---------------- SORTING ----------------
def selectionSort(arr):
    # Repeatedly find smallest item and put it in the front
    for i in range(len(arr)-1):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]  # swap
    return arr


def insertionSort(arr):
    # Insert each item into its correct place in sorted part
    for i in range(1, len(arr)):
        cur, j = arr[i], i
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = cur
    return arr


def bubbleSort(arr):
    # Keep swapping neighbours until list is sorted
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# ---------------- SEARCHING ----------------
def linearSearch(arr, target):
    # Check each item one by one
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binaryIterSearch(arr, target):
    # Binary search using loop (array must be sorted)
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target: return mid
        elif arr[mid] < target: l = mid+1
        else: r = mid-1
    return -1


def binaryRecurSearch(arr, l, r, target):
    # Binary search using recursion
    if l <= r:
        mid = (l+r)//2
        if arr[mid]==target: return mid
        elif arr[mid]<target:
            return binaryRecurSearch(arr, mid+1, r, target)
        else:
            return binaryRecurSearch(arr, l, mid-1, target)
    return -1


def ternarySearch(arr, l, r, target):
    # Split array into 3 parts instead of 2
    if l <= r:
        mid1 = l + (r-l)//3
        mid2 = r - (r-l)//3
        if arr[mid1]==target: return mid1
        if arr[mid2]==target: return mid2
        if target < arr[mid1]:
            return ternarySearch(arr, l, mid1-1, target)
        elif target > arr[mid2]:
            return ternarySearch(arr, mid2+1, r, target)
        else:
            return ternarySearch(arr, mid1+1, mid2-1, target)
    return -1


# ---------------- TESTING ----------------
if __name__ == "__main__":
    # Test Stack
    s = Stack()
    s.push(10); s.push(20)
    print("Stack peek:", s.peek())      # should be 20
    print("Stack pop:", s.pop())        # removes 20
    print("Stack length:", s.length())  # should be 1

    # Test Queue
    q = Queue()
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    print("Queue peek:", q.peek())      # should be 1
    print("Queue dequeue:", q.dequeue())# removes 1
    print("Queue length:", q.length())  # should be 2

    # Test Circular Queue
    cq = CircularQueue(3)
    cq.enqueue(5); cq.enqueue(6); cq.enqueue(7)
    print("CircularQueue dequeue:", cq.dequeue())  # removes 5
    cq.enqueue(8)
    print("CircularQueue state:", cq.data)         # shows [8,6,7] in some form

    # Test reverse_queue
    q2 = Queue()
    for i in [1,2,3,4]: q2.enqueue(i)
    reverse_queue(q2)
    print("Reversed queue data:", q2.data)  # should be [4,3,2,1]

    # Test remove_adjacent
    print("Remove adj (abbccd):", remove_adjacent("abbccd"))     # -> ad
    print("Remove adj (dsallasg):", remove_adjacent("dsallasg")) # -> dg

    # Test bracket_check
    print("Brackets (abc):", bracket_check("(abc)"))   # True
    print("Brackets wrong:", bracket_check("[a{b]c}")) # False

    # Test Sorting
    arr = [64, 25, 12, 22, 11]
    print("Selection sort:", selectionSort(arr.copy()))
    print("Insertion sort:", insertionSort(arr.copy()))
    print("Bubble sort:", bubbleSort(arr.copy()))

    # Test Searching
    sorted_arr = [1,2,3,4,5,6,7,8,9]
    print("Linear search 5:", linearSearch(sorted_arr, 5)) # index 4
    print("BinaryIter search 5:", binaryIterSearch(sorted_arr, 5))
    print("BinaryRecur search 5:", binaryRecurSearch(sorted_arr, 0, len(sorted_arr)-1, 5))
    print("Ternary search 5:", ternarySearch(sorted_arr, 0, len(sorted_arr)-1, 5))
