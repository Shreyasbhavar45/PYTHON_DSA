def reverseEachword(s):
    rev = s.split()
    f = rev[::-1]
    return " ".join(f)

s = ' hello wordl'
r =reverseEachword(s)
print(r)

      