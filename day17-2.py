from aoc_common import addDictList

targetX=range(94,151+1)
targetY=range(-156,-103+1)

xStep={}
yStep={}
xEnd={}


for x in range(max(targetX)+2):
    step=x
    now=0
    serial=0
    while step>=-1:
        serial+=1
        now+=step
        if now in targetX:
            addDictList(xStep, serial, x)
        step-=1
    if now in targetX:
        addDictList(xEnd, serial, x)

for y in range(min(targetY), min(targetY)*-1+2):
    step=y
    now=0
    serial=0
    while step>=min(targetY):
        serial+=1
        now+=step
        if now in targetY:
            addDictList(yStep, serial, y)
        step-=1
    # print(now,step)

result=set()


print(xStep)
print(yStep)
print(xEnd)

for i,j in yStep.items():
    print(i,j)
    if i in xStep:
        for x in xStep[i]:
            for y in yStep[i]:
                result.add((x,y))
    for k in xEnd:
        if i>=k:
            print(i,k)
            for x in xEnd[k]:
                for y in yStep[i]:
                    result.add((x,y))


print(result)
print(len(result))

print(xStep)
print(yStep)
print(xEnd)