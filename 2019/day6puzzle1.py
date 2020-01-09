import os

working_directory = os.path.dirname(__file__)
input_file_path = working_directory + '/day6input.txt'

adjacencyList = {}
totalFuel = 0
modTotFuel = 0
with open(input_file_path) as fp:
    for line in fp:
        nodes = line.split(")")
        if nodes[0] in adjacencyList:
            adjNodes = adjacencyList.get(nodes[0])
            adjNodes.append(nodes[1].strip())
        else:
            adjacencyList[nodes[0]] = [nodes[1].strip()]
        
    # print(adjacencyList)

count = 0
visited = []
queue = [["COM"]]
while len(queue) > 0:
    # print(queue)
    path = queue.pop(0)
    lastNode = path[-1]
    visited.append(lastNode)
    if lastNode in adjacencyList.keys():
        for node in adjacencyList[lastNode]:
            if node not in visited:
                newPath = list(path)
                newPath.append(node)
                queue.append(newPath)
                count+= len(path)

print(count)
