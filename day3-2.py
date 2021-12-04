file=open("day3.txt")
bitFrequency=[]
count=0
codes=[]
while True:
    thisline = file.readline().strip()
    if not thisline:
        break
    count+=1
    codes.append(thisline)
oxygen=codes.copy()
co2=codes.copy()
for i in range(len(codes[0])):
    # print(oxygen)
    tempCount=0
    for j in oxygen:
        tempCount+=int(j[i])
    tempStatus=1 if tempCount>=len(oxygen)/2 else 0
    oxygen=list(filter(lambda x: int(x[i])==tempStatus,oxygen))
    print(tempStatus, tempCount, len(oxygen))
    if len(oxygen)==1:
        break
for i in range(len(codes[0])):
    tempCount=0
    for j in co2:
        tempCount+=int(j[i])
    tempStatus=1 if tempCount<len(co2)/2 else 0
    print(tempStatus, tempCount, len(co2))
    co2=list(filter(lambda x: int(x[i])==tempStatus,co2))
    if len(co2)==1:
        break
print(int(co2[0],2)*int(oxygen[0],2))