file=open("day9.txt")
heightmap=[]
visited=[]
while True:
    thisline = file.readline()
    if not thisline:
        break
    heightmap.append([int(i) for i in list(thisline.strip())])

count=0
for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        if i-1<0 or heightmap[i-1][j]>heightmap[i][j]:
            if j-1<0 or heightmap[i][j-1]>heightmap[i][j]:
                if i+1>=len(heightmap) or heightmap[i+1][j]>heightmap[i][j]:
                    if j+1>=len(heightmap[i]) or heightmap[i][j+1]>heightmap[i][j]:
                        count+=1+heightmap[i][j]
                        print(heightmap[i][j])
print(count)