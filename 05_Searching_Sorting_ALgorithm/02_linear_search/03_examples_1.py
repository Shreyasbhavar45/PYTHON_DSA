#linear_search([3, 7, 2, 5], 2,54) should return 2
def linear_search(arr,target):
    size = len(arr)
    for index in range(0,size):
        if(arr[index]==target):
            return index
        
    return -1
my_list =[3,7,2,5,8,7]
target = 8
result = linear_search(my_list,target)
print(result)