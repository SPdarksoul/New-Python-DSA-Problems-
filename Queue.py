class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        return self.queue[0]

    def rear(self):
        if self.is_empty():
            raise IndexError("Rear from an empty queue")
        return self.queue[-1]

    def size(self):
        return len(self.queue)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # Output: 1
    print(q.front())    # Output: 2
    print(q.rear())     # Output: 3
    print(q.size())     # Output: 2
