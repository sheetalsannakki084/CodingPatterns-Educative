




def hascycle(graph):
    visited=set()
    rec=set()

    for node in graph:
        if node not in visited:
            if dfs(graph,node,visited,rec):
                return True
    return False


def dfs(graph,node,visited,rec):
    visited.add(node)
    rec.add(node)

    for child in graph[node]:
        if child not in visited:
            if dfs(graph,child,visited,rec):
                return True
        elif child in rec:
            return True

    rec.remove(node)
    return False




graph = {
    "a": ["b","c","d"],
    "b": ["d"],
    "c": [],

    "d": []

}
obj=hascycle(graph)
if obj:
    print("has cycle")
else:
    print("no cycle")