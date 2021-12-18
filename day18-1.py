from aoc_common import fileToArray
from copy import deepcopy
class Num:
    def __init__(self, val, depth):
        self.val=val
        self.depth=depth

    def __repr__(self):
        return f"Num({self.val}, {self.depth})"


def concat(arr1, arr2):
    for i in range(len(arr1)):
        arr1[i].depth+=1
    for i in range(len(arr2)):
        arr2[i].depth+=1
    return arr1 + arr2

def calculate(arr):
    completeFlag=False
    while completeFlag==False:
        # print(arr)
        completeFlag=True
        for i in range(len(arr)):
            if arr[i].depth>4:
                if i-1 in range(len(arr)):
                    arr[i-1].val+=arr[i].val
                if i+2 in range(len(arr)):
                    arr[i+2].val+=arr[i+1].val
                arr.pop(i)
                arr[i].val=0
                arr[i].depth-=1
                completeFlag=False
                break
        if completeFlag==True:
            for i in range(len(arr)):
                if arr[i].val>=10:
                    value=arr[i].val//2
                    rest=arr[i].val%2
                    arr[i].val=value+rest
                    arr[i].depth+=1
                    arr.insert(i, Num(value, arr[i].depth))
                    completeFlag=False
                    break
    return arr

def calculation(incoming):
    arr=deepcopy(incoming)
    while len(arr)>1:
        i=0
        while i<len(arr):
            if arr[i].depth==arr[i+1].depth:
                arr[i].val=arr[i].val*3 + arr[i+1].val*2
                arr[i].depth-=1
                arr.pop(i+1)
                break
            i+=1
    return arr

def flattening(arr):
    outputArr=[]
    string=list(arr)
    depth=0
    for i in string:
        if i == "[":
            depth+=1
        elif i=="]":
            depth-=1
        elif i==",":
            pass
        else:
            outputArr.append(Num(int(i),depth))
    return outputArr


puzzle=fileToArray("day18.txt")
# print(puzzle)
result=None

for i in puzzle:
    toBeAdded=flattening(i)
    # print(toBeAdded)
    if result==None:
        result=toBeAdded
    else:
        result=concat(result, toBeAdded)
    # print(result)
    result=calculate(result)
    # print(result)

print (calculation(result))