# ---------------- STACK ----------------
class Stack:
    def __init__(self, max_size=10):
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

    def peek(self):  # Look at the top item
        if self.top == -1: raise IndexError
        return self.data[self.top]

    def length(self):  # Number of items
        return self.top + 1


# ---------------- QUEUE ----------------
class Queue:
    def __init__(self, max_size=10):
        self.data, self.head, self.tail, self.max_size = [], 0, -1, max_size

    def enqueue(self, item):  # Add item at back
        if self.tail == self.max_size - 1: raise OverflowError
        self.tail += 1
        self.data.insert(self.tail, item)

    def dequeue(self):  # Remove from front
        if self.tail == -1: raise IndexError
        item = self.data[self.head]
        for i in range(self.head, self.tail):
            self.data[i] = self.data[i+1]
        del self.data[self.tail]
        self.tail -= 1
        return item

    def peek(self):  # Look at the front item
        if self.tail == -1: raise IndexError
        return self.data[self.head]

    def length(self):  # Number of items
        return self.tail + 1


# ---------------- CIRCULAR QUEUE ----------------
class CircularQueue:
    def __init__(self, max_size=5):
        self.data, self.head, self.tail, self.max_size = [None]*max_size, 0, 0, max_size

    def isEmpty(self): return self.head == self.tail
    def isFull(self): return (self.tail - self.head == self.max_size)

    def enqueue(self, item):  # Add at tail
        if self.isFull(): raise OverflowError
        self.data[self.tail % self.max_size] = item
        self.tail += 1

    def dequeue(self):  # Remove at head
        if self.isEmpty(): raise IndexError
        item = self.data[self.head % self.max_size]
        self.head += 1
        return item


# ---------------- TWIST FUNCTIONS ----------------
def binaryClosestSearch(arr, target):
    # Binary search that returns closest value if not found
    l, r = 0, len(arr) - 1
    closest = arr[0]
    while l <= r:
        mid = (l + r) // 2
        if abs(arr[mid] - target) < abs(closest - target):
            closest = arr[mid]
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return closest


def bubbleSortWithSteps(arr):
    # Bubble sort with print after each pass
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"Pass {i+1}: {arr}")
    return arr


def reverseQueueRecursive(q):
    # Reverse queue using recursion
    if q.length() == 0:
        return
    item = q.dequeue()
    reverseQueueRecursive(q)
    q.enqueue(item)


def remove_adjacent_queue(s):
    # Remove adjacent duplicates using queue
    from collections import deque
    q = deque()
    for ch in s:
        if q and q[-1] == ch:
            q.pop()
        else:
            q.append(ch)
    return "".join(q)


def bracket_check_queue(expr):
    # Check brackets using queue
    from collections import deque
    q = deque()
    pairs = {')':'(', ']':'[', '}':'{'}
    for ch in expr:
        if ch in pairs.values():
            q.append(ch)
        elif ch in pairs:
            if not q or q.pop() != pairs[ch]:
                return False
    return len(q) == 0


def stack_min_max(stack):
    # Find min and max in a stack
    if stack.length() == 0:
        return None, None
    return min(stack.data), max(stack.data)


def selectionSortDesc(arr):
    # Selection sort descending order
    for i in range(len(arr)-1):
        max_i = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_i]:
                max_i = j
        arr[i], arr[max_i] = arr[max_i], arr[i]
    return arr


def middle_of_queue(q):
    # Find middle element of queue
    size = q.length()
    for _ in range(size // 2):
        q.dequeue()
    return q.peek()


# ---------------- TESTING ----------------
if __name__ == "__main__":
    # BinaryClosestSearch
    nums = [1, 3, 5, 8, 10, 15]
    print("Closest to 6:", binaryClosestSearch(nums, 6))   # 5
    print("Closest to 9:", binaryClosestSearch(nums, 9))   # 8
    print("Closest to 15:", binaryClosestSearch(nums, 15)) # 15

    # BubbleSortWithSteps
    arr = [5, 1, 4, 2]
    print("Bubble Sort with steps:")
    bubbleSortWithSteps(arr.copy())

    # Queue + reverseQueueRecursive
    q = Queue()
    for i in [1, 2, 3, 4]: q.enqueue(i)
    reverseQueueRecursive(q)
    print("Reversed queue (recursive):", q.data)

    # remove_adjacent_queue
    print("Remove adj queue (abbccd):", remove_adjacent_queue("abbccd"))   # ad
    print("Remove adj queue (dsallasg):", remove_adjacent_queue("dsallasg")) # dg

    # bracket_check_queue
    print("Bracket check queue (abc):", bracket_check_queue("(abc)"))    # True
    print("Bracket check queue wrong:", bracket_check_queue("[a{b]c}")) # False

    # stack_min_max
    s = Stack()
    s.push(10); s.push(5); s.push(30)
    print("Stack min/max:", stack_min_max(s))  # (5, 30)

    # selectionSortDesc
    arr = [64, 25, 12, 22, 11]
    print("Selection sort descending:", selectionSortDesc(arr.copy()))

    # middle_of_queue
    q2 = Queue()
    for i in [1, 2, 3, 4, 5]: q2.enqueue(i)
    print("Middle of queue:", middle_of_queue(q2))  # 4
    
