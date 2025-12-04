def star_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2*i - 1))

star_pyramid(5)