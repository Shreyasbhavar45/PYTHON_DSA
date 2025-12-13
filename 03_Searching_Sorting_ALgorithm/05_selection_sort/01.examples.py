'''Selection Sort works by repeatedly finding the minimum element from the unsorted part 
of the list and swapping it with the first element of the unsorted part.'''

def selection_sort(arr):
    n =len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if (arr[j]< arr[min_index]):
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]

    return arr
    
unselection_sort = [64, 25, 12, 22, 11]
result = selection_sort(unselection_sort)
print(result)