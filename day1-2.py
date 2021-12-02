file=open("input.txt")
count = 0
array= []
currentWindow=0
previousWindow=0
countLarge=0
while True:
    thisline = file.readline()
    if not thisline:
        break
    array.append(thisline)
    count+=1
    if count>3:
        previousWindow=currentWindow
        currentWindow=currentWindow+int(thisline)-int(array[count-4])
        if currentWindow-previousWindow>0:
            countLarge+=1
    else:
        currentWindow+=int(thisline)
    if count<100:
        print(currentWindow,previousWindow,count, thisline)
print(countLarge)