s = 'mainacademy'
d = {}
for c in s:
    d.setdefault(c, s.count(c))
print(d)