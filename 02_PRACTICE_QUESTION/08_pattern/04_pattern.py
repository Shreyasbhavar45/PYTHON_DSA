#right angled triangle
def right_angled_triangle(n):
    for i in range(1, n + 1):  # rows
        for j in range(i):     # columns
            print("*", end=" ")
        print() 
         # new line after each row


# Taking input from user
n = int(input("Enter the number of rows: "))
right_angled_triangle(n)
