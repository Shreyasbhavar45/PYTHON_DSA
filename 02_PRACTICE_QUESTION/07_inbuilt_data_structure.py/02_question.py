#largest
def largest(arr):
    largest_num = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest_num:
            largest_num=arr[i]

    return largest_num
    
num = [3,11,33,7, 2, 9,8,8,9,8,10]
result=largest(num)
print(result)
    