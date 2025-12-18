'''You are given a list of integers. 
Write a Python program that reverses the list without using slicing (lst[::-1]). 
The program should return the reversed list.'''

def reverse_list(arr):
    arr.reverse()
    return arr

nums = [1,2,3,4,5]
result = reverse_list(nums)
print(result)