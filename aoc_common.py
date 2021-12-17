def fileToArray(filename, returnInt=False):
    output=[]
    file=open(filename)
    while True:
        thisline = file.readline().strip()
        if not thisline:
            break
        if returnInt==True:
            thisline=int(thisline)
        output.append(thisline)
    return output

def fileToMap(filename, sep, returnInt=False):
    input=fileToArray(filename)
    output=[]
    for i in input:
        if sep=="":
            line=list(i)
        else:
            line=i.split(sep)
        if returnInt==True:
            line=[int(element) for element in line]
        output.append(line)
    return output

def addDictList(obj, key, value):
    if key in obj:
        obj[key].append(value)
    else:
        obj[key]=[value]

def addDict(obj, key, value):
    if key in obj:
        obj[key]+=value
    else:
        obj[key]=value