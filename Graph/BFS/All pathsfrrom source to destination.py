from collections import deque


def dfs(graph,s,d,path):
    result=[]

    stack=[(s,[s])]

    while stack:
        node,path=stack.pop()

        if node==d:
            result.append(path.copy())
            continue
        for child in graph[node]:
            if child not in path:
                newpath=path+[child]
                stack.append((child,newpath))
    return result


# in stack not only node will copy tht path also with child
def bfs(graph,s,d):
    result=[]

    # queue=[] we ucan use this but while pop we shd use queue.pop(o)-pop frm front
    queue=deque([(s,[s])])

    while queue:
        node,path =queue.popleft()

        if node==d:
            result.append(path.copy())
            continue
        for child in graph[node]:
            if child not in path:
                newpath=path+[child]
                queue.append((child,newpath))
    return result








graph = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "f"],
    "d": ["b", "g"],
    "e": ["b"],
    "f": ["c", "h"],
    "g": ["d"],
    "h": ["f","g"]}

s="a"
d="g"

obj=dfs(graph,s,d,[])
print("dfs paths are",obj)
obj1=bfs(graph,s,d)
print("paths are",obj1)
