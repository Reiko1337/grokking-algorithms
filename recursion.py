def sum_list(arr: list) -> int:
    if len(arr) == 0:
        return 0
    else:
        return arr.pop(0) + sum_list(arr)


# print(sum_list([1, 5, 10, 4, 5]))


def count_list(arr: list) -> int:
    if not arr:
        return 0
    else:
        arr.pop()
        return 1 + count_list(arr)


# print(count_list([1, 5, 10, 4, 5, 3]))


def max_list(arr: list) -> int:
    if len(arr) == 1:
        return arr[0]
    else:
        a = arr.pop()
        b = max_list(arr)
        return b if a < b else a


# print(max_list([1, 5, 120, 4, 5, 3, -2]))


def binary_search(arr: list, item: int) -> list:
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2
    guess = arr[mid]
    if guess == item:
        return mid
    else:
        if guess > item:
            binary_search(arr[low:mid - 1], item)
        else:
            binary_search(arr[mid + 1:high], item)


print(binary_search([1, 5, 120, 4, 5, 3, -2], 3))
