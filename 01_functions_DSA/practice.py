n = 121345
original = n
rev = 0
for digit in str(n)[::-1]:
    rev = rev*10+int(digit)


if rev==original:
    print('palindrome')
else:
    print('not palindrome')