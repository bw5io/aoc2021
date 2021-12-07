file=open("input7.txt")
locations = file.readline().strip().split(",")
locations = [int(i) for i in locations]
print(min([sum([abs(i-x) for i in locations])for x in range(min(locations), max(locations))]))
