'''You are given a list of integers. 
Write a Python program that checks if all
 elements in the list are unique.
 If all elements are unique, return True; 
otherwise, return False.'''
def check_unique(arr):
    freq = {}
    for num in arr:
        if num in freq:
            return False
        freq[num] = 1
    return True

freq = [1,2,3,4,5,]# if there is repeat no there is false else return

print(check_unique(freq))
