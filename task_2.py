some_dict = {'a':5, 'b':3, 'c':4, 'd':10}
multiply = 1
for value in some_dict.values():
    multiply *= value
print(multiply)