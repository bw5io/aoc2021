file=open("day10.txt")
pairing={"(": ")", "[": "]", "{": "}", "<": ">"}
score_step1={")": 3, "]": 57, "}": 1197, ">":25137}
score_step2={"(": 1, "[": 2, "{": 3, "<":4}
step1_result=0
step2_result=[]
while True:
    thisline = file.readline()
    if not thisline:
        break
    stack=[]
    illegal=0
    line_result=0
    line=list(thisline.strip())
    for i in line:
        if i in pairing:
            stack.append(i)
        else:
            if pairing[stack.pop()]!=i:
                step1_result+=score_step1[i]
                illegal=1
                break
    if not illegal:
        while stack:
            line_result*=5
            line_result+=score_step2[stack.pop()]
        step2_result.append(line_result)
step2_result.sort()
print(step1_result)
print(step2_result[len(step2_result)//2])