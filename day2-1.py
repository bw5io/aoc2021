file=open("day2.txt")
mark={}
aim=0
while True:
    thisline = file.readline()
    if not thisline:
        break
    temp=thisline.strip().split(" ")
    print(temp)
    if temp[0] in mark:
        mark[temp[0]]+=int(temp[1])
    else:
        mark[temp[0]]=int(temp[1])
print(mark["forward"]*(mark["up"]-mark["down"]))