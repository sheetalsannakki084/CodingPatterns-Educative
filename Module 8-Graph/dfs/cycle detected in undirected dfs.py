
def hascycle(graph):
    visited=set()

    for node in graph:
        if node not in visited:
            if dfs(graph,node,visited,None):
                return True

    return False

def dfs(graph,node,visited,parent):
    visited.add(node)
    for child in graph[node]:
            if child not in visited:
                if dfs(graph,child,visited,node):
                    return True
            elif child!=parent:
                return True

    return False





graph = {
    "a": ["c", "b"],
    "b": ['a', 'd'],
    "c": ['a'],
    "d": ["b","a"]}

obj=hascycle(graph)
print("it has cycle?",obj)
