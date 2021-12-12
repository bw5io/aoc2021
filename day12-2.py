from aoc_common import fileToArray

def searchRoute(obj, currentNode, visited, repeatVisit):
    result=0
    if currentNode=="end":
        # print (visited)
        return 1
    for i in obj[currentNode]:
        if i not in visited or repeatVisit==0 or all(j.isupper() for j in i):
            thisVisit=visited.copy()
            # if all(j.islower() for j in i):
            thisVisit.append(i)
            result+=searchRoute(obj, i, thisVisit, 1 if i in visited and all(j.islower() for j in i) else repeatVisit)
    return result




routes=fileToArray("test12.txt")
connections={}
for i in routes:
    connection=i.split("-")
    if connection[1]!="start" and connection[0]!="end":
        if connection[0] in connections:
            connections[connection[0]].append(connection[1])
        else:
            connections[connection[0]]=[connection[1]]
    if connection[0]!="start" and connection[1]!="end":
        if connection[1] in connections:
            connections[connection[1]].append(connection[0])
        else:
            connections[connection[1]]=[connection[0]]
print(connections)
print(searchRoute(connections, "start", ["start"], 0))