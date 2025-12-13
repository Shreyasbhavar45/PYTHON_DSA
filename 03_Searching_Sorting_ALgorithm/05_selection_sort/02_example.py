def selection_sort(arr):
    n =len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if (arr[j]< arr[min_index]):
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]

    return arr
    
unselection_sort = [29,12,54,78,92,45]
result = selection_sort(unselection_sort)
print(result)

##how it Works:-

'''1️⃣ Which function is used where?
selection_sort(arr)

This is a function

It takes a list arr

It sorts the list

It returns the sorted list

len(arr)
n = len(arr)


len() → counts how many elements are in the list

Here:

arr = [64, 25, 12, 22, 11]
n = 5

2️⃣ Outer loop → for i in range(n-1)
for i in range(n-1):


👉 This loop decides which position we are filling

i = 0 → fill 1st position

i = 1 → fill 2nd position

i = 2 → fill 3rd position

i = 3 → fill 4th position

We don’t need the last element because it will already be sorted.

3️⃣ min_index = i (Very Important)
min_index = i


👉 We assume the current element is the smallest.

Example when i = 0:

min_index = 0
value = 64

4️⃣ Inner loop → for j in range(i+1, n)
for j in range(i+1, n):


👉 This loop searches for the smallest element in the remaining list.

🔁 Dry Run (STEP BY STEP)
🟢 PASS 1 (i = 0)

Array: [64, 25, 12, 22, 11]

min_index = 0 → value = 64

Compare:

25 < 64 → YES → min_index = 1

12 < 25 → YES → min_index = 2

22 < 12 → NO

11 < 12 → YES → min_index = 4

✅ Smallest found = 11

Swap:

arr[0], arr[4] = arr[4], arr[0]


Array becomes:

[11, 25, 12, 22, 64]

🟢 PASS 2 (i = 1)

Array: [11, 25, 12, 22, 64]

min_index = 1 → value = 25

Compare:

12 < 25 → YES → min_index = 2

22 < 12 → NO

64 < 12 → NO

Swap:

[11, 12, 25, 22, 64]

🟢 PASS 3 (i = 2)

Array: [11, 12, 25, 22, 64]

min_index = 2 → value = 25

Compare:

22 < 25 → YES → min_index = 3

64 < 22 → NO

Swap:

[11, 12, 22, 25, 64]

🟢 PASS 4 (i = 3)

Array: [11, 12, 22, 25, 64]

min_index = 3

Compare with 64 → already smallest

No change.

5️⃣ Swap line (only ONCE per pass)
arr[i], arr[min_index] = arr[min_index], arr[i]


👉 This is Python tuple swapping
👉 No temp variable needed

6️⃣ return arr
return arr


Sends the sorted array back

7️⃣ Function Call
result = selection_sort(unselection_sort)
print(result)


Output:

[11, 12, 22, 25, 64]

🧠 One-Line Logic (VERY IMPORTANT)

Selection Sort = find the smallest element and put it in the correct place'''