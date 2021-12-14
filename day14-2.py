import collections
from typing import Collection


file=open("day14.txt")
polymer=file.readline().strip()
file.readline()
rules={}
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
    if toBeCompared in pairing:
        pairing[toBeCompared]+=1
    else:
        pairing[toBeCompared]=1
    pointer+=1

for i in range(40):
    newPairing={}
    for i,j in pairing.items():
        if i in rules:
            left=i[0]+rules[i]
            right=rules[i]+i[1]
            if left in newPairing:
                newPairing[left]+=j
            else:
                newPairing[left]=j
            if right in newPairing:
                newPairing[right]+=j
            else:
                newPairing[right]=j
            if rules[i] in counter:
                counter[rules[i]]+=j
            else:
                counter[rules[i]]=j
        else:
            newPairing[i]=j
    print(counter)
    print(newPairing)
    pairing=newPairing
    print(max(counter.values())-min(counter.values()))