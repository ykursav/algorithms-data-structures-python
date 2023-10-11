class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp_val = self.head
        while temp_val is not None:
            print(temp_val.value)
            temp_val = temp_val.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
            self.head = None

        return temp

    def pop_first(self):
        if self.length == 0:
            return None

        tmp = self.head
        self.head = self.head.next
        tmp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return tmp

    def insert(self, index, value):
        ...

    def get(self, index):
        ...


my_linked_list = LinkedList(4)

my_linked_list.append(3)
my_linked_list.append(6)
# print(my_linked_list.print_list())
# my_linked_list.pop()
# print(my_linked_list.print_list())

# my_linked_list.pop()
# print(my_linked_list.print_list())
# my_linked_list.pop()
# print(my_linked_list.print_list())
# my_linked_list.pop()
# print(my_linked_list.print_list())

my_linked_list.prepend(7)
my_linked_list.print_list()
