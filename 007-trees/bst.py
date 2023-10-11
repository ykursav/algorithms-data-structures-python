# left always smaller than parent
# right always bigger than parent
# Insert O(logn) - linked list O(1)
# Remove O(logn) - linked list O(n)
# Lookup O(logn) - linked list O(n)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if temp.value == value:
                return False

            if value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left

    def contains(self, value):
        temp = self.root
        if self.root is None:
            return False

        while temp is not None:
            if temp.value == value:
                return True

            if value > temp.value:
                temp = temp.right
            else:
                temp = temp.left

        return False


##########################################################
##   Test code below will print output to "User logs"   ##
##########################################################


def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")


print("\n----- Test: Insert to Empty Tree -----\n")
bst = BinarySearchTree()
result = bst.insert(5)
check(True, result, "Insert 5, should succeed:")
check(5, bst.root.value, "Root value after inserting 5:")
check(None, bst.root.left, "Root's left child after inserting 5:")
check(None, bst.root.right, "Root's right child after inserting 5:")

print("\n----- Test: Insert to Existing Tree -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
result = bst.insert(3)
check(True, result, "Insert 3, should succeed:")
check(3, bst.root.left.left.value, "Root's left-left value after inserting 3:")
check(None, bst.root.left.left.left, "Root's left-left-left child after inserting 3:")
check(None, bst.root.left.left.right, "Root's left-left-right child after inserting 3:")

print("\n----- Test: Insert Duplicate Value -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
result = bst.insert(5)
check(False, result, "Insert 5 again, should fail:")
check(None, bst.root.left.left, "Root's left-left child after inserting 5 again:")
check(None, bst.root.left.right, "Root's left-right child after inserting 5 again:")

print("\n----- Test: Insert Greater Than Root -----\n")
bst = BinarySearchTree()
bst.insert(10)
result = bst.insert(15)
check(True, result, "Insert 15, should succeed:")
check(15, bst.root.right.value, "Root's right value after inserting 15:")
check(None, bst.root.right.left, "Root's right-left child after inserting 15:")
check(None, bst.root.right.right, "Root's right-right child after inserting 15:")

print("\n----- Test: Insert Less Than Root -----\n")
bst = BinarySearchTree()
bst.insert(10)
result = bst.insert(5)
check(True, result, "Insert 5, should succeed:")
check(5, bst.root.left.value, "Root's left value after inserting 5:")
check(None, bst.root.left.left, "Root's left-left child after inserting 5:")
check(None, bst.root.left.right, "Root's left-right child after inserting 5:")
