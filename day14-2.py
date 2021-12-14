import collections
from datetime import datetime

def addDict(obj, key, value):
    if key in obj:
        obj[key]+=value
    else:
        obj[key]=value

rules={}

file=open("day14.txt")
polymer=file.readline().strip()
file.readline()
while True:
    thisline = file.readline()
    if not thisline:
        break
    thisline=thisline.strip().split(" -> ")
    rules[thisline[0]]=thisline[1]

counter=dict(collections.Counter(polymer))

pointer=0
pairing={}
while pointer<len(polymer)-1:
    toBeCompared=polymer[pointer:pointer+2]
    addDict(pairing, toBeCompared, 1)
    pointer+=1

for number in range(40):
    start = datetime.now()
    newPairing={}
    for i,j in pairing.items():
        if i in rules:
            left=i[0]+rules[i]
            right=rules[i]+i[1]
            addDict(newPairing, left, j)
            addDict(newPairing, right, j)
            addDict(counter, rules[i], j)
        else:
            newPairing[i]=j
    pairing=newPairing
    print(f"Round {number+1}: {max(counter.values())-min(counter.values())}. Elapsed Time: {datetime.now()-start}")