def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


def item_in_common_efficient(list1, list2):
    dict1 = {}
    for elem in list1:
        dict1[elem] = True

    for elem in list2:
        if dict1.get(elem):
            return True

    return False


list1 = [1, 3, 5]
list2 = [2, 4, 6]

print(item_in_common(list1, list2))
print(item_in_common_efficient(list1, list2))
