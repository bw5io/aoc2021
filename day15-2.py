from aoc_common import fileToMap
from copy import deepcopy
from datetime import datetime
start = datetime.now()
def findShortest(obj, scMap, st=[]):
    st.append([0,0,0])
    while st:
        current = st.pop(0)
        x,y=current[0],current[1]
        fourDirections=[(1,0),(0,1),(-1,0),(0,-1)]
        for i,j in fourDirections:
            if i+x in range(len(scMap)) and j+y in range(len(scMap)):
                length=scMap[x][y]+obj[i+x][j+y]
                if length<scMap[i+x][j+y] or scMap[i+x][j+y]==-1:
                    scMap[i+x][j+y]=length
                    st.append([i+x,j+y,length])
        st.sort(key=lambda x: x[2])
    return scMap[-1][-1]
    
    

ogMap=fileToMap("day15.txt", '',True)
# print(ogMap)
xMap=deepcopy(ogMap)
# for x in xMap:
#     print("".join([str(i) for i in x]))

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
# for x in yMap:
#     print("".join([str(i) for i in x]))
smap=[[-1 for _ in range(len(yMap[1]))] for _ in range(len(yMap))]
smap[0][0]=0
print(findShortest(yMap,smap))
print(f"Elapsed Time: {datetime.now()-start}")