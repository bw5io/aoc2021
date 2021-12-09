def checkBasin(heightmap, location, visited):
    i,j = location
    if  i<0 or i>=len(heightmap) or j<0 or j>=len(heightmap[i]) or visited[i][j]==1:
        return 0
    elif heightmap[i][j]==9:
        visited[i][j]=1
        return 0
    else:
        returnValue=0
        visited[i][j]=1
        returnValue+=checkBasin(heightmap,(i-1,j), visited)
        returnValue+=checkBasin(heightmap,(i+1,j), visited)
        returnValue+=checkBasin(heightmap,(i,j+1), visited)
        returnValue+=checkBasin(heightmap,(i,j-1), visited)
    return returnValue+1

basin=[]
file=open("day9.txt")
heightmap=[]

while True:
    thisline = file.readline()
    if not thisline:
        break
    heightmap.append([int(i) for i in list(thisline.strip())])

visited=[[0 for _ in i] for i in heightmap]

for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        if (i,j) not in visited:
            result = checkBasin(heightmap, (i,j), visited)
            if result!=0:
                basin.append(result)
basin.sort()
# print(basin)
print(basin[-1]*basin[-2]*basin[-3])
print(len(heightmap),len(heightmap[0]))