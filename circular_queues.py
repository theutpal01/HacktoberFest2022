from sys import maxsize


class Queue:
    def __init__(self, cap):
        self.queue = [None] * cap
        self.capacity = cap
        self.front = -1
        self.rear = -1
        self.curr_size = 0

    def is_full(self):
        return (self.front == self.rear + 1) or (self.front == 0 and self.rear == self.capacity - 1)

    def is_empty(self):
        return self.front == -1

    def enqueue(self, item):
        if self.is_full():
            print("Can't add the queue is full ")

        else:
            if self.front == -1:
                self.front = 0

            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
            print(item, " was added")

    def dequeue(self):
        item = None
        if self.is_empty():
            print("Can't add the queue is empty")
            return -maxsize
        else:
            item = self.queue[self.front]

            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.capacity

            print(item, " dequeued")
            return item

    # function to display the queue
    def display(self):
        i = 0
        if self.is_empty():
            print("Empty Queue")
        else:
            print("\nQueue: ")
            i = self.front
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.capacity

            print(self.queue[i])


# Driver Code
q = Queue(6)
q.dequeue()  # Underflow condition

q.enqueue(12)
q.enqueue(14)
q.enqueue(16)
q.enqueue(18)
q.enqueue(20)

q.display()
q.dequeue()
q.dequeue()

q.display()

q.enqueue(22)
q.enqueue(24)
q.enqueue(26)
q.enqueue(28)  # Overflow condition
q.display()
