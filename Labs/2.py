from collections import deque

class SimpleQueue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print("Front ->", list(self.items), "<- Rear")

q = SimpleQueue()
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
q.display()

print("Peek (Front):", q.peek())
print("Rear:", q.rear())
print("Dequeued:", q.dequeue())
q.display()
print("Size:", q.size())