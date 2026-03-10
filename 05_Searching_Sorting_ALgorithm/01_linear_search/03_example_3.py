#linear_search([], 5) should return -1
def linear_search(arr,target):
    size =len(arr)
    for index in range(0,size):
        if(arr[index]==target):
            return index
        
    return -1
my_list =[]
target = 5
result = linear_search(my_list,target)
print(result)