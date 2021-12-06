from collections import Counter
from datetime import datetime
now=datetime.now()
file=open("test6.txt")
fishes = file.readline().strip().split(",")
fishes=[int(i) for i in fishes]
fishesDict=dict(Counter(fishes))
fishesDict[-1]=0

print(fishesDict)
for i in range(80):
    for i in range(0,9):
        fishesDict[i-1]=fishesDict[i] if i in fishesDict else 0
    fishesDict[6]+=fishesDict[-1]
    fishesDict[8]=fishesDict[-1]
    print(fishesDict, sum(fishesDict.values())-fishesDict[-1])
print(sum(fishesDict.values())-fishesDict[-1])
current=datetime.now()
print(current-now)