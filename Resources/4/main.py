class Stack:
    def __init__(self, max_size=None):
        self.stack = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        if self.max_size is None or self.max_size == 0:
            return False
        return len(self.stack) == self.max_size

    def push(self, item):
        if self.is_full():
            raise Exception('Stack is full')
        self.stack.append(item)
        print(f"Pushed {item}")

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty, cannot peek')
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        print(f"Top to bottom: {self.stack[::-1]}")


max_size = int(input("Enter max size: "))
s = Stack(max_size)

for i in range(1, max_size + 1):
    s.push(i)

print(f"Is stack full? {s.is_full()}")
print(f"Top element is: {s.peek()}")
print(f"Popped element is: {s.pop()}")
print(f"Stack size is: {s.size()}")
print(f"Is stack empty? {s.is_empty()}")
s.display()