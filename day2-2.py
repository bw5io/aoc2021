file=open("day2.txt")
depth=0
position=0
aim=0
while True:
    thisline = file.readline()
    if not thisline:
        break
    temp=thisline.strip().split(" ")
    print(temp)
    if temp[0]=="forward":
        position+=int(temp[1])
        depth+=int(temp[1])*aim
    elif temp[0]=="up":
        aim+=int(temp[1])
    elif temp[0]=="down":
        aim-=int(temp[1])
print(depth*position)