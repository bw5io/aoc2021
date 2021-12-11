def fileToArray(filename):
    output=[]
    file=open(filename)
    while True:
        thisline = file.readline().strip()
        if not thisline:
            break
        output.append(thisline)
    return output
