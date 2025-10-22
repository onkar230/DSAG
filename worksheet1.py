# ===============================
# DSALG Worksheet 1 – Stacks & Queues
# ===============================

# ---------- Queue ----------
class Queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = -1
        self.max_size = 15

    def enqueue(self, newData):
        print("Enqueue the data " + str(newData))
        if self.tail == self.max_size - 1:
            raise OverflowError("Cannot insert into a full queue.")
        self.tail += 1
        self.data.insert(self.tail, newData)
        print("Now the tail index is " + str(self.tail))

    def dequeue(self):
        if self.tail == -1:
            raise IndexError("Cannot delete from an empty queue.")
        removed = self.data[self.head]
        print("Dequeue the data " + str(removed))
        temp = self.head
        while temp < self.tail:
            temp += 1
            self.data[temp - 1] = self.data[temp]
        del self.data[temp]
        self.tail -= 1
        return removed

    def peek(self):
        if self.tail == -1:
            raise IndexError("Cannot peek from an empty queue.")
        print("Peek the head")
        return self.data[self.head]

    def length(self):
        return self.tail + 1

    def print_message(self):
        print("The queue size is " + str(self.length()) + 
              " The first element is " + str(self.peek()))

    def print_all(self):
        while self.tail != -1:
            print(self.dequeue())

    def reverse(self):
        print("\nBefore reverse, the queue is ", self.data)
        stack = Stack()
        while self.length() > 0:
            element = self.dequeue()
            stack.push(element)
        while stack.length() > 0:
            element = stack.pop()
            self.enqueue(element)
        print("\nThe reversed queue is ", self.data)


# ---------- Stack ----------
class Stack:
    def __init__(self):
        self.data = []
        self.top = -1
        self.max_size = 5

    def push(self, newData):
        print("Push the data " + str(newData))
        if self.top == self.max_size - 1:
            raise OverflowError("Cannot insert into a full stack.")
        self.top += 1
        self.data.insert(self.top, newData)
        print("Now the top index is " + str(self.top))

    def pop(self):
        if self.top == -1:
            raise IndexError("Cannot delete from an empty stack.")
        removed = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        print("Pop the data " + str(removed))
        return removed

    def peek(self):
        if self.top == -1:
            raise IndexError("Cannot peek from an empty stack.")
        print("Peek the top")
        return self.data[self.top]

    def length(self):
        return self.top + 1

    def print_message(self):
        print("The stack size is " + str(self.length()) + 
              " The top element is " + str(self.peek()))

    def print_all(self):
        while self.top != -1:
            print(self.pop())

    def remove_adjacent(self, input_str):
        print("\nThe input string is: ", input_str)
        result = ""
        for character in input_str:
            if self.length() > 0 and self.peek() == character:
                self.pop()
            else:
                self.push(character)
        s_temp = Stack()
        while self.length() > 0:
            element = self.pop()
            s_temp.push(element)
        while s_temp.length() > 0:
            result = result + s_temp.pop()
        print("\nThe string after removing adjacent duplicates is: ", result)
        return result

    def bracket_check(self, input_str):
        print("\nThe input string is: ", input_str)
        pairs = {')': '(', '}': '{', ']': '['}
        for character in input_str:
            if character in pairs.values():
                self.push(character)
            elif character in pairs:
                if self.length() == 0 or self.peek() != pairs[character]:
                    return False
                self.pop()
        return self.length() == 0


# ---------- Circular Queue ----------
class CircularQueue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0
        self.max_size = 5

    def enqueue(self, newData):
        if self.tail - self.head == self.max_size:
            raise OverflowError("Cannot insert into a full circular queue.")
        print("Enqueue the data " + str(newData))
        ind_tail = self.tail % self.max_size
        self.tail += 1
        if ind_tail < len(self.data):
            self.data[ind_tail] = newData
        else:
            self.data.insert(ind_tail, newData)
        print("Now the new tail is " + str(self.tail) + 
              " The index used for the tail is " + str(ind_tail))

    def dequeue(self):
        if self.tail == self.head:
            self.data = []
            self.head = 0
            self.tail = 0
            raise IndexError("Cannot delete from an empty circular queue.")
        ind_head = self.head % self.max_size
        self.head += 1
        removed = self.data[ind_head]
        print("Dequeue the data " + str(removed))
        print("Now the new head is " + str(self.head) + 
              " The index used for the head is " + str(ind_head))
        return removed

    def peek(self):
        if self.tail == self.head:
            raise IndexError("Can't peek from an empty queue")
        print("Peek the head")
        ind_head = self.head % self.max_size
        return self.data[ind_head]

    def length(self):
        return self.tail - self.head

    def print_message(self):
        print("The circular queue size is " + str(self.length()) +
              " The first element is " + str(self.peek()) +
              " The head ind is now " + str(self.head) +
              " The tail ind is now " + str(self.tail))

    def print_all(self):
        while self.tail != self.head:
            print(self.dequeue())


# ===============================
# Test cases
# ===============================
if __name__ == "__main__":
    # Queue
    q = Queue()
    for j in range(10, 20):
        q.enqueue(50 - j)
        q.print_message()
    for i in range(10, 16):
        q.dequeue()
        q.print_message()
    q.print_all()

    # Stack
    s = Stack()
    for i in range(1, 6):
        s.push(i)
        s.print_message()
    for i in range(1, 3):
        s.pop()
        s.print_message()
    s.print_all()

    # Reverse Queue
    q2 = Queue()
    for i in range(0, 5):
        q2.enqueue(i)
    q2.reverse()

    # Circular Queue
    cq = CircularQueue()
    for k in range(5):
        cq.enqueue(k)
        cq.print_message()
    for i in range(3):
        cq.dequeue()
        cq.print_message()

    # Remove Adjacent Duplicates
    s2 = Stack()
    s2.remove_adjacent("dsallasg")
    s2.remove_adjacent("abccbadd")

    # Bracket Check
    s3 = Stack()
    print("(abc) is valid? ", s3.bracket_check("(abc)"))
    s4 = Stack()
    print("d[sa]l(g) is valid? ", s4.bracket_check("d[sa]l(g)"))
    s5 = Stack()
    print("[a{b]c} is valid? ", s5.bracket_check("[a{b]c}"))
