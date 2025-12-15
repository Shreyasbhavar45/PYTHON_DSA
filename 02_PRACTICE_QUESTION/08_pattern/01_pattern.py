#Square of side 'N'
def square_area(n):
    n = 5
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()#moves to next line.
square_area(6)
