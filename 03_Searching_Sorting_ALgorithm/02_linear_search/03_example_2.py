#linear_search([1, 1, 2, 1], 1) should return 0
def linear_search(arr,target):
    size = len(arr)
    for index in range(0,size):
        if(arr[index]==target):
            return index
        
    return -1
my_list = [1,1,2,1]
target = 2
result =linear_search(my_list,target)
print(result)