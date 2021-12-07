from collections import Counter

def plusTo(x, cache):
    if x in cache:
        return cache[x]
    output=0
    for i in range(x+1):
        output+=i
    cache[x]=output
    return output
file=open("input7.txt")
locations = file.readline().strip().split(",")
locations = [int(i) for i in locations]
cache={}
print(min([sum([plusTo(abs(i-x), cache) for i in locations])for x in range(min(locations), max(locations))]))

