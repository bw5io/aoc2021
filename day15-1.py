from typing import Counter
from aoc_common import fileToMap
# import sys
# sys.setrecursionlimit(100000)


def findShortest(obj, x, y, scMap, maxnumber=0, queue=[]):
    # print(x,y)
    if x==len(scMap)-1 and y==len(scMap[x])-1:
        return
    fourDirections=[(1,0),(0,1)]
    for i,j in fourDirections:
        if i+x in range(len(scMap)) and j+y in range(len(scMap)):
            length=scMap[x][y]+obj[i+x][j+y]
            if length<scMap[i+x][j+y] or scMap[i+x][j+y]==-1:
                scMap[i+x][j+y]=length
                findShortest(obj,x+i,y+j,scMap,maxnumber,queue)
    


ogMap=fileToMap("day15.txt", '',True)
# print(ogMap)

sQueue=[]
start=(0,0)

lengthmap=[[-1 for _ in range(len(ogMap[1]))] for _ in range(len(ogMap))]
lengthmap[0][0]=0
# print(lengthmap)
x,y=0,0
findShortest(ogMap,x,y,lengthmap)
print(lengthmap)
