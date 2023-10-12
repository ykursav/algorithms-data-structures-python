# Big O
# Appending O(1)
# Get O(1) -> Worst possible O(n) not very possible


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []

        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return self.data_map[index]

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])

        return all_keys


hash_table = HashTable()
hash_table.set_item("washers", 1400)
hash_table.set_item("bolts", 50)
print(hash_table.get_item("washers"))
print(hash_table.get_item("bolts"))
print(hash_table.get_item("lumber"))

print(hash_table.keys())
