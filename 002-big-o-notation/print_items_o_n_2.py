
# o(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

if __name__ == "__main__":
    print_items(10)