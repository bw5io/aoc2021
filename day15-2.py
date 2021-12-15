from aoc_common import fileToMap
from copy import deepcopy

ogMap=fileToMap("test15.txt", '',True)
# print(ogMap)
xMap=deepcopy(ogMap)
for x in xMap:
    print("".join([str(i) for i in x]))

for i in range(4):
    for x in range(len(ogMap)):
        for y in range(len(ogMap[x])):
            ogMap[x][y]=ogMap[x][y]+1 if ogMap[x][y]+1<10 else 1
            xMap[x].append(ogMap[x][y])

yMap=deepcopy(xMap)
for i in range(4):
    newMap=[]
    for x in range(len(xMap)):
        newLine=[]
        for y in range(len(xMap[x])):
            xMap[x][y]=xMap[x][y]+1 if xMap[x][y]+1<10 else 1
            newLine.append(xMap[x][y])
        newMap.append(newLine)
    yMap+=newMap


smap=[[-1 for _ in range(len(yMap[1]))] for _ in range(len(yMap))]
smap[0][0]=0
x,y=0,0