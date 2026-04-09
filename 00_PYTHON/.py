arr = [1, 0, 2]
for i in range(len(arr)):
    for j in range(i + 1, len(arr) + 1):
        subarray = arr[i:j]
        print(subarray)
