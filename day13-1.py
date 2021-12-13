

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

folding(coordinates, foldRules[0])

map={}
for i in coordinates:
    if i[0] not in map:
        map[i[0]]=set()
    map[i[0]].add(i[1])
print(foldRules, coordinates, map)
result=0
for i in map.values():
    print(len(i))
    result+=len(i)
print(result)