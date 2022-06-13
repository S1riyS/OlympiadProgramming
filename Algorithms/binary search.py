def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        middle = (left + right) // 2
        if data[middle] == target:
            return middle
        elif data[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def main():
    A = [1, 2, 3, 5, 7, 10, 12, 112, 123, 235, 651]
    target = 12
    print(binary_search(data=A, target=target))


if __name__ == '__main__':
    main()
