class Queue:
    def __init__(self, capacity=None):
        self.items = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        if self.capacity is None:
            return False
        return len(self.items) >= self.capacity

    def enqueue(self, x):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.items.append(x)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def size(self):
        return len(self.items)

    def display(self):
        print("Front ->", self.items, "<- Rear")

q = Queue(4)
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
q.display()

print("Front element:", q.front())
print("Dequeued element:", q.dequeue())
q.display()