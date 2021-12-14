import collections
from typing import Collection


file=open("test14.txt")
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
for i in range(10):
    pointer=0
    while pointer<len(polymer)-1:
        toBeCompared=polymer[pointer:pointer+2]
        if toBeCompared in rules.keys():
            polymer=polymer[0:pointer+1]+rules[toBeCompared]+polymer[pointer+1:]
            pointer+=1
        pointer+=1
    # print(polymer)
result = collections.Counter(polymer)
print(max(result.values())-min(result.values()))