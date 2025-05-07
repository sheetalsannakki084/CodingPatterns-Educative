def solution(graph,nodes,s):
    visited=set()
    count=0

    for i in range(len(nodes)):
        if i not in visited:
            count += 1
            dfs(graph,nodes,i,visited)

    return count


def dfs(graph,nodes,s,visited):
    stack=[]

    stack.append(s)
    while stack:
        nodex=stack.pop()

        if nodex not in visited:
            visited.add(nodex)
            # print(nodes[nodex])


            for child in range(len(graph[nodex])):
                if graph[nodex][child]==1 and child not in visited:
                    stack.append(child)


# Test it
graph = [
    [0, 1, 0,0],
    [1, 0, 0,0],
    [0, 0, 0,0],
    [0, 0, 0,0],

]
nodes = ["a", "b", "c","d"]
s = "a"
obj = solution(graph, nodes, s)
print(obj)

