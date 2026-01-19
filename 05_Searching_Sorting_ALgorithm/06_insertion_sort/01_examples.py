'''Insertion Sort works by building a sorted section of the list, one element at a time,
by inserting each new element into its proper position within the already sorted section.'''

def insertion_sort(arr):
    n =len(arr)
    for current in range(1,n):
        currentCard =arr[current]
        correctPosition =current-1#it will go from i-1

        while correctPosition >= 0:
            if(arr[correctPosition]< currentCard):
                break
            else:
                arr[correctPosition +1]=arr[correctPosition]
                correctPosition -=1

            arr[correctPosition +1]= currentCard

    return arr


uninsertion_sort =[12, 11, 13, 5, 6]
result =insertion_sort(uninsertion_sort)
print(result)