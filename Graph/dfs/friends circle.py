

def solution(graph):
    visited=set()
    count=0

    for s in graph:
        if s not in visited:
            count+=1
            dfs(graph,s,count,visited)
    return count

def dfs(graph,s,count,visited):
    stack=[s]
    while stack:
        node=stack.pop()

        if node not in visited:
            visited.add(node)


            for child in graph[node]:
                if child not in visited:
                    stack.append(child)








graph={"a":["b","d"],
       "b":["a"],
       "c":["e"],
       "d":["a"],
       "e":["c"],
       "f":[]}

#
# graph={1:[],
#        2:[],
#        3:[]}
#        # 3:[4],
#        # 4:[3]}




obj=solution(graph)
print(obj)