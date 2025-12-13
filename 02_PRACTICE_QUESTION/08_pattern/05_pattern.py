#inverted right triangle.
def inverted_right_triangle(n):#9
    for i in range(n, 0, -1):
        print("*" * i)

# Taking input
n = int(input("Enter the number of rows: "))
inverted_right_triangle(n)