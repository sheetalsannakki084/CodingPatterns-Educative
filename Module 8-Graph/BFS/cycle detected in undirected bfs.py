from collections import deque
def hascycle(graph):
    visited=set()

    for node in graph:
        if node not in visited:
            if bfs(node,graph,visited,None):
                return True
    return False




def bfs(node,graph,visited,parent):
    q = deque([(node, None)])

    while q:
        node,parent=q.popleft()

        if node not in visited:
            visited.add(node)

            for child in graph[node]:
                if child not in visited:
                    q.append((child,node))

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

