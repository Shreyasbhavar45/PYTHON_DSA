#decreasing pattern.
def increase_pattern(n):
    for i in range(n):
        for j in range(i,n):
            print("*",end = " ")
        print()
        
increase_pattern(6)