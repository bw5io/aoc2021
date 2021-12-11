def flash(object, x, y, flashed):
    goThrough=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i,j in goThrough:
        if x+i in range(len(object)) and y+j in range(len(object[x+i])) and (x+i,y+j) not in flashed:
            object[x+i][y+j]+=1
            if object[x+i][y+j]>9:
                flashed.append((x+i,y+j))
                flash(object, x+i, y+j, flashed)
    return object


file=open("day11.txt")
map=[]
result=0
while True:
    thisline = file.readline()
    if not thisline:
        break
    map.append([int(i) for i in list(thisline.strip())])
i=0
while True:
    i+=1
    flashed=[]
    counter=0
    for j in range(len(map)):
        for k in range(len(map[j])):
            map[j][k]+=1
            if map[j][k]>9 and (j,k) not in flashed:
                flashed.append((j,k))
                flash(map,j,k,flashed)
    for j,k in flashed:
        if map[j][k]!=0:
            counter+=1
            map[j][k]=0
    if counter==len(map)*len(map[0]):
        print(i)
        break
