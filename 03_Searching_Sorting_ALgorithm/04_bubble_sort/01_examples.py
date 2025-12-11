## bubble sort :- is the way to sort the elements in ascending order. 
## like example[120,25,11,34,90,22] itss answer is [11,22,25,34,90,120]
def bubble_sort(arr):
    n = len(arr)
    for passes in range(0,n):

        for j in range(0,n-1-passes):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]


    return arr
            
unsorted_list =[120,25,11,34,90,22,67] 
result = bubble_sort(unsorted_list)  
print("sorted list is:",result)   
   