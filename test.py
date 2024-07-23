def binary_search(sorted_list, target, compare_func):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if compare_func(sorted_list[mid], target):
            low = mid + 1
        elif compare_func(target, sorted_list[mid]):
            high = mid - 1
        else:
            return mid

    return -1

#Example usage:
num_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

def less_than(a, b):
    return a < b

def equal_to(a, b):
    return a == b

target = 13
index = binary_search(num_list, target, less_than)
if index != -1:
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found in the list")

target = 15
index = binary_search(num_list, target, equal_to)
if index != -1:
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found in the list")
