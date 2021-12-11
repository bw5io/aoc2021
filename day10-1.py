file=open("day10.txt")
pairing={"(": ")", "[": "]", "{": "}", "<": ">"}
score_step1={")": 3, "]": 57, "}": 1197, ">":25137}
result=0
while True:
    thisline = file.readline()
    if not thisline:
        break
    stack=[]
    line=list(thisline.strip())
    print(line)
    for i in line:
        if i in pairing:
            stack.append(i)
        else:
            if pairing[stack.pop()]!=i:
                result+=score_step1[i]
print(result)