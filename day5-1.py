def validateOverlap(x, y, route, duplicate):
    if x in route:
        if y in route[x]:
            duplicate.add(str(x)+","+str(y))
            return (route, duplicate)
        else:
            route[x].append(y)
    else:
        route[x]=[y]
    return (route,duplicate)

file=open("test5.txt")
passedRoutes={}
duplicate=set()
overlapRoutes=0
while True:
    thisline = file.readline()
    if not thisline:
        break
    coordinates=thisline.strip().split(" -> ")
    left=coordinates[0].split(",")
    right=coordinates[1].split(",")
    for i in range(2):
        left[i]=int(left[i])
        right[i]=int(right[i])
    if left[0]==right[0]:
        print(0)
        for i in range(min(left[1],right[1]),max(left[1],right[1])+1):
            passedRoutes, overlapCounts = validateOverlap(left[0], i, passedRoutes, duplicate)
    elif left[1]==right[1]:
        print(1)
        for i in range(min(left[0],right[0]),max(left[0],right[0])+1):
            passedRoutes, overlapCounts = validateOverlap(i, left[1], passedRoutes, duplicate)

    print(coordinates)
print(passedRoutes, duplicate, len(duplicate))