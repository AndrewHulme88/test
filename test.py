arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def compare(x, y):
    return x - y

index = binary_search(arr, 5, compare)
print(index)  # Output: 4

def compare_str(x, y):
    if x < y:
        return -1
    elif x == y:
        return 0
    else:
        return 1

arr_str = ["apple", "banana", "cherry", "date", "elderberry"]
index = binary_search(arr_str, "date", compare_str)
print(index)  # Output: 3
