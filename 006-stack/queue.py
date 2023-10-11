# FIFO
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        temp = Node(value)

        if self.length == 0:
            self.first = temp
            self.last = temp
        else:
            self.last.next = temp
            self.last = temp

        self.length += 1

        return temp

    def dequeue(self):
        if self.length == 0:
            return None

        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next

        temp.next = None
        self.length -= 1
        return temp


my_queue = Queue(4)

print("First:", my_queue.first.value)
print("Last:", my_queue.last.value)
print("Length:", my_queue.length)


"""
    EXPECTED OUTPUT:
    ----------------
    First: 4
    Last: 4
    Length: 1

"""

print(my_queue.print_queue())

my_queue = Queue(1)

print("Queue before enqueue(2):")
my_queue.print_queue()

my_queue.enqueue(2)

print("\nQueue after enqueue(2):")
my_queue.print_queue()


"""
    EXPECTED OUTPUT:
    ----------------
    Queue before enqueue(2):
    1

    Queue after enqueue(2):
    1
    2

"""
