#right sided triangle
'''
increasing space
decreasing star

'''
def right_side(n):
    for i in range(n):
        for j in range(i+1):
            print(" ",end ="  ")
        for j in range(i,n):
            print("*",end="  ")
        print()

right_side(5)