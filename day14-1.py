import collections
from datetime import datetime

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
# print(rules)
for number in range(40):
    start=datetime.now()
    pointer=0
    while pointer<len(polymer)-1:
        toBeCompared=polymer[pointer:pointer+2]
        if toBeCompared in rules.keys():
            polymer=polymer[0:pointer+1]+rules[toBeCompared]+polymer[pointer+1:]
            pointer+=1
        pointer+=1
    counter = collections.Counter(polymer)
    print(f"Round {number+1}: {max(counter.values())-min(counter.values())}. Elapsed Time: {datetime.now()-start}")
    # print(polymer)
result = collections.Counter(polymer)
    