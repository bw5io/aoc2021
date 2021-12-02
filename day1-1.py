file=open("input.txt")
count = 0
previousline=0
result=0
while True:
    thisline = file.readline()
    if not thisline:
        break
    count+=1
    if count>1:
        result+=((int(thisline)-int(previousline))>0)
        previousline=thisline
print(result)