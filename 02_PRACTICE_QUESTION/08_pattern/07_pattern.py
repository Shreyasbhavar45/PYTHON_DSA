def inverted_pyramid(n):
    for i in range(n):
        # leading spaces
        print(" " * i, end=" ")
        # stars
        print("* " * (n - i))

# Example
n = int(input("Enter n: "))
inverted_pyramid(n)