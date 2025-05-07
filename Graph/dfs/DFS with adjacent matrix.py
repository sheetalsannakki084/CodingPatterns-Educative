

def solution(graph,node,s):
    visited=set()
    stack=[]
    startindx=node.index(s)
    stack.append(startindx)
    while stack:
        nodex=stack.pop()

        if nodex not in  visited:
            visited.add(nodex)
            print(node[nodex])

            for child in range(len(graph[nodex])):
                if graph[nodex][child]==1 and child not in visited:
                    stack.append(child)






graph = [
    [0, 1, 1, 0, 0, 0, 0],  # a
    [1, 0, 0, 1, 0, 0, 0],  # b
    [1, 0, 0, 0, 0, 0, 0],  # c
    [0, 1, 0, 0, 1, 1, 0],  # d
    [0, 0, 0, 1, 0, 0, 0],  # e
    [0, 0, 0, 1, 0, 0, 1],  # f
    [0, 0, 0, 0, 0, 1, 0]   # g
]
nodes = ["a", "b", "c", "d", "e", "f", "g"]
s = "a"  # Starting node

obj=solution(graph,nodes,s)
print(obj)