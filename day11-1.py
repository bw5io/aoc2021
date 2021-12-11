def flash(object, x, y, flashed):
    goThrough=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i,j in goThrough:
        # print(x+i,y+j)
        if x+i in range(len(object)) and y+j in range(len(object[x+i])) :
            # print("Triggered")
            object[x+i][y+j]+=1
            if object[x+i][y+j]==10:
                flashed.append((x+i,y+j))
                flash(object, x+i, y+j, flashed)
    # print(object)
    return object


file=open("day11.txt")
map=[]
result=0
while True:
    thisline = file.readline()
    if not thisline:
        break
    map.append([int(i) for i in list(thisline.strip())])

for i in range(100):
    flashed=[]
    print(map)
    for j in range(len(map)):
        for k in range(len(map[j])):
            map[j][k]+=1
            if map[j][k]==10:
                flashed.append((j,k))
                flash(map,j,k,flashed)
    print(flashed)
    for j,k in flashed:
        result+=1
        map[j][k]=0
    print(result)