d = {i:i**3 for i in range(1, 11)}
print(d)

some_list_1 = [1, 3, 4, 6, 8, 10]
some_list_2 = ['a', 'c', 'd', 'b', 'r', 'd']
d2 = {}
for i in range(len(some_list_1)):
    d2[some_list_1[i]] = some_list_2[i]
print(d2)

d3 = dict(zip(some_list_1, some_list_2))
print(d3)
