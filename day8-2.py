file=open("day8.txt")
numberDict={2:1, 4:4, 3:7, 7:8}
deciphered={}
counter=0
result=0
while True:
    deciphered={}
    identifier={}
    thisline = file.readline()
    if not thisline:
        break
    splitted=thisline.split("|")
    output=splitted[1].strip().split(" ")
    allnumber=splitted[0].strip().split(" ")+splitted[1].strip().split(" ")
    # Create Dictionary for 1,4,7,8
    for i in allnumber:
        if len(i) in numberDict:
            if i not in deciphered:
                deciphered[i]=numberDict[len(i)]
                if len(i)==2:
                    identifier[1]=list(i)
                if len(i)==4:
                    identifier[4]=list(i)
    identifier[4]=[x for x in identifier[4] if x not in identifier[1]]
    # Decipher the rest
    for k in allnumber:
        if k not in deciphered:
            i=list(k)
            ident1=len(list(j for j in i if j in identifier[1]))
            ident4=len(list(j for j in i if j in identifier[4]))
            if len(i)==5:
                if ident1==2:
                    deciphered[k]=3
                elif ident4==2:
                    deciphered[k]=5
                elif ident4==1:
                    deciphered[k]=2
            elif len(i)==6:
                if ident1==1:
                    deciphered[k]=6
                elif ident4==2:
                    deciphered[k]=9
                else:
                    deciphered[k]=0
    # Decipher
    outputlist=[]
    for i in output:
        outputlist.append(str(deciphered[i]))
    result+=int("".join(outputlist))
print(result)