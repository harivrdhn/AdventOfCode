import os

working_directory = os.path.dirname(__file__)
input_file_path = working_directory + '/day6input.txt'

adjacencyList = {}
totalFuel = 0
modTotFuel = 0
with open(input_file_path) as fp:
    for line in fp:
        nodes = line.split(")")
        nodes2 = nodes[1].strip()
        if nodes[0] in adjacencyList:
            adjNodes = adjacencyList.get(nodes[0])
            adjNodes.append(nodes2)
        else:
            adjacencyList[nodes[0]] = [nodes2]

        if nodes2 in adjacencyList:
            adjNodes = adjacencyList.get(nodes2)
            adjNodes.append(nodes[0])
        else:
            adjacencyList[nodes2] = [nodes[0]]
        
    # print(adjacencyList)


myPath = []
visited = []
start = adjacencyList["YOU"]
end = adjacencyList["SAN"]
queue = [start] 
while len(queue) > 0:
    # print(queue)
    path = queue.pop(0)
    lastNode = path[-1]
    if (lastNode == end[0]): 
        myPath = path
        break
    visited.append(lastNode)
    if lastNode in adjacencyList.keys():
        for node in adjacencyList[lastNode]:
            if node not in visited:
                newPath = list(path)
                newPath.append(node)
                queue.append(newPath)



print( "transfers required = " + str(len(myPath)))

