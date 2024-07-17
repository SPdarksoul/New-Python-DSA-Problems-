# Count of Frequency
arr = [22, 22, 33, 44, 233, 44, 3, 23, 3, 3, 3, 3, 3]
print(arr)

d = {}
for item in arr:
    d[item] = d.get(item, 0) + 1

print(d)


#Min And Max

maxCount  =0
maxValue = -1

minCount = 100000
minvalue = None

for key,count in d.items():
   if count > maxCount:
     maxCount = count
     maxValue = key
   if minCount > count:
      minCount = count
      minValue = key

print(maxCount,maxValue)
print(minCount,minValue)
