#Square of side 'N'
def square_area(n):
    area = n * n
    return area

n = int(input("Enter the side of the square: "))

result = square_area(n)

print("Area of square is:", result)