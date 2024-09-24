x = 125 + 25**3 + 5**9
print(x)
s = ''
while x > 0:
    s = str(x%5) + s
    x //= 5
print(s)
print(int(s,5))
print(s.count('0'))

