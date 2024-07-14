arr = [22, 22, 33, 44, 233, 44, 3, 23, 3, 3, 3, 3, 3]
print(arr)

d = {}
for item in arr:
    d[item] = d.get(item, 0) + 1

print(d)
