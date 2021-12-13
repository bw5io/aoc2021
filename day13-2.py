

output=[]
file=open("day13.txt")
foldRules=[]
coordinates=[]
while True:
    thisline = file.readline()
    if not thisline:
        break
    if "," in thisline:
        coordinates.append([int(i) for i in list(thisline.strip().split(","))])
    elif "fold" in thisline:
        foldRule=thisline.strip().split("=")
        foldRule[1]=int(foldRule[1])
        foldRules.append([foldRule[0][-1],foldRule[1]])

def folding(obj, rule):
    tbc=0 if rule[0]=="x" else 1
    for i in range(len(obj)):
        if obj[i][tbc]>rule[1]:
            obj[i][tbc]=obj[i][tbc]-(obj[i][tbc]-rule[1])*2

def createMap(obj):
    map={}
    for i in obj:
        if i[0] not in map:
            map[i[0]]=set()
        map[i[0]].add(i[1])
    return map

def backToCoordinates(obj):
    coordinates=[]
    for i,j in obj.items():
        for k in j:
            coordinates.append([i,k])
    return coordinates

for i in foldRules:
    folding(coordinates, i)
    map=createMap(coordinates)
    coordinates=(backToCoordinates(map))

print(coordinates)
result=0
for i in map.values():
    result+=len(i)
print(result)

maxx=max(map.keys())
print(maxx)
maxy=max(max(i) for i in map.values())
print(maxy)
canvas=[["." for _ in range(maxx+1)]for _ in range(maxy+1)]
for i in coordinates:
    canvas[i[1]][i[0]]="#"
for i in canvas:
    print("".join(i))
