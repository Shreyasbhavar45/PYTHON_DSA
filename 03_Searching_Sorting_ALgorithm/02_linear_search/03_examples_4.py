#linear_search([4, 2, 8], 6) should return -1
def linear_search(arr,target):
    size =len(arr)
    for index in range(0,size):
        if(arr[index]==index):
            return index
        
    return -1
my_list = [4,2,8]
target = 6
target = 9
result = linear_search(my_list,target)
print(result)