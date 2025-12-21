'''Count Even and Odd Numbers in a List
You are given a list f integers.
 Write a Python program that counts and 
 returns the number of even and odd numbers in the list.'''

def count_even_or_odd(arr):
   even_count = 0
   odd_count = 0
   for i in arr:
      if i%2==0:
        even_count+=1
      else:
        odd_count+=1

   return even_count,odd_count


lst = [1, 2, 3, 4, 5]
even,odd =count_even_or_odd(lst)
print('even',even)
print('odd',odd)