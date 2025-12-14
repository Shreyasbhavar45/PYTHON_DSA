'''check if all elements are in list are unique'''
def check_unique(arr):
    freq = {}
    for num in arr:
        if num in freq:
            return False
        freq[num] = 1
    return True

freq = [1,2,3,4,5]

print(check_unique(freq))
