#increasing Triangle pattern.
def increase_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end = " ")
        print()

increase_pattern(5)