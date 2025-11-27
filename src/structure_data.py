class Stack:
    def __init__(self, capacity=100):
        self.data = [None] * capacity
        self.capacity = capacity
        self.top = 0

    def push(self, value):
        if self.top >= self.capacity:
            raise OverflowError("стек полон")
        self.data[self.top] = value
        self.top += 1

    def pop(self):
        if self.top <= 0:
            raise IndexError("стек пуст")
        self.top -= 1
        value = self.data[self.top]
        self.data[self.top] = None
        return value

    def is_empty(self):
        return self.top == 0

    def size(self):
        return self.top

    def peek(self):
        if self.top == 0:
            raise IndexError("стек пуст")
        return self.data[self.top - 1]


class Queue:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self._size = 0

    def enquene(self, value):
        if self._size == self.capacity:
            raise OverflowError("очередь переполнена")
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self._size += 1

    def dequene(self):
        if self._size == 0:
            raise IndexError("очередь пуста")
        value = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self._size -= 1
        return value

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def peek(self):
        if self._size == 0:
            raise IndexError("очередь пуста")
        return self.data[self.head]

my_stack = Stack(5)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
my_stack.push(7)
print(my_stack.pop())






