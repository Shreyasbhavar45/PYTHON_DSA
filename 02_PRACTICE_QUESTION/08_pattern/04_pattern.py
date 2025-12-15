#right angled triangle
def right_angled_triangle(n):
    for i in range(n):
        for j in range(i,n):
            print('  ',end='')
        for j in range(i+1):
            print('*',end =' ')

        print()
right_angled_triangle(8)
