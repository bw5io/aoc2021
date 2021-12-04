file=open("day3.txt")
bitFrequency=[]
count=0
while True:
    thisline = file.readline().strip()
    if not thisline:
        break
    count+=1
    for i,j in enumerate(thisline):
        if count==1:
            bitFrequency.append(int(j))
        else:
            bitFrequency[i]+=int(j)
doubler=1
gamma=0
epsilon=0
for i in range(len(bitFrequency)-1,-1,-1):
    gamma+=doubler*int(bitFrequency[i]>count/2)
    epsilon+=doubler*int(bitFrequency[i]<=count/2)
    doubler*=2
print(gamma*epsilon)