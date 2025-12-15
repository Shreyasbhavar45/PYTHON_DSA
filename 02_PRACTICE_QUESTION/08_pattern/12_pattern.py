#hill pattern
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
decresing space 
increasing star
increasing star

'''
def hill_pattern(n):
    for i in range(n):
        for j in range(i+n):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
hill_pattern(4)