def consecutive_max_numbers(arr):
    max_diff = 0

    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])

        if diff > max_diff:
            max_diff = diff

    return max_diff


lst = [1, 7, 3, 10, 5]
print(consecutive_max_numbers(lst))