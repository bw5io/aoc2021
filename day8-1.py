file=open("day8.txt")
numberDict={1:2,4:4,8:7,7:3}
counter=0
while True:
    thisline = file.readline()
    if not thisline:
        break
    thisline=thisline.split("|")
    numbers=thisline[1].strip().split(" ")
    print(numbers)
    for i in numbers:
        if len(i) in numberDict.values():
            counter+=1
print(counter)