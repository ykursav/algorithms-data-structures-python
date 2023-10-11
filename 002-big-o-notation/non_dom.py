
# o(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)

if __name__ == "__main__":
    print_items(10)