dict = {}
dict2 = {}
while True:
    s = list(input().split(', '))
    if s[0] == "конец":
        break
    if s[0] in dict:
        dict[s[0]] += [int(s[1])]
    else:
        dict[s[0]] = [int(s[1])]
for items in dict:
    result = sum(dict[items])/len(dict[items])
    dict2[items] = result
for i in sorted(dict2.items(), key = lambda para: (-para[1], para[0])):
    print(*i)