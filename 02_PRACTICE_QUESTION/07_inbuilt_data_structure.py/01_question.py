'''Sum of List Elements'''
def sum_of_list(arr):
    total = 0
    for num in arr:
        total = total + num
    return total

print(sum_of_list([1, 2, 3, 4, 5]))