def checkBingo(obj):
    for i in obj:
        if sum(i)==0:
            return True
    for i in range(5):
        if sum([obj[x][i] for x in range(5)])==0:
            return True
    return False


file=open("test4.txt")
bingoSequence = file.readline().strip().split(",")

for i in range(len(bingoSequence)):
    bingoSequence[i]=int(bingoSequence[i])

# print(bingoSequence)
file.readline()
bingoCards=[]
bingoCard=[]

while True:
    thisline = file.readline()
    if not thisline:
        break
    if not thisline.strip():
        bingoCards.append(bingoCard)
        bingoCard=[]
    else:
        bingoCard.append(thisline.strip().split())
bingoCards.append(bingoCard)
# print(bingoCards)

lowestCount=len(bingoSequence)
answer=0

for i in bingoCards:
    count=0
    temp=0
    bingoMap={}
    for j in range(5):
        for k in range(5):
            i[j][k]=int(i[j][k])
    for j,k in enumerate(i):
        for l,m in enumerate(k):
            bingoMap[m]=[j,l]
    # print(bingoMap)
    for j in bingoSequence:
        count+=1
        if j in bingoMap.keys():
            # print("BINGO")
            loc=bingoMap[j]
            temp=i[loc[0]][loc[1]]
            i[loc[0]][loc[1]]=0
            if checkBingo(i):
                break
    # print(count, temp)
    print(i)
    if count<lowestCount:
        lowestCount=count
        answer = temp * sum(sum(line) for line in i)
        print(count,answer)

print(lowestCount,answer)


