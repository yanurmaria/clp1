# Problem 1: Maximum of three using if-elif-else
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# Problem 2: Digit count and digit sum
def digit_count_and_sum(n):
    n = abs(n)  # handle negative numbers
    if n == 0:
        return 1, 0

    count = 0
    digit_sum = 0

    while n > 0:
        digit = n % 10
        digit_sum += digit
        count += 1
        n //= 10

    return count, digit_sum


# Problem 3: Bubble sort + Binary search
def binary_search_with_bubble_sort(arr, target):
    n = len(arr)

    # Bubble sort
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Binary search
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ---------------- MAIN PROGRAM ----------------

# Problem 1
a, b, c = map(int, input("Enter three integers: ").split())
print("Maximum value:", max_of_three(a, b, c))

# Problem 2
num = int(input("Enter an integer: "))
count, total = digit_count_and_sum(num)
print("Digit count:", count)
print("Digit sum:", total)

# Problem 3
arr = list(map(int, input("Enter list elements: ").split()))
target = int(input("Enter target value: "))
result = binary_search_with_bubble_sort(arr, target)
print("Search result index:", result)
