


def dfs(graph,s,d,path):

    # result=[]
    # stack=[(s,[s])]
    #
    #
    # while stack:
    #     node,path=stack.pop()
    #
    #
    #
    #     if node==d:
    #         result.append(path.copy())
    #         continue
    #     for child in graph[node]:
    #         if child not in path:
    #             newpath=path+[child]
    #             stack.append([child,newpath])
    # return result
    #

    result=[]
    q=[]
    q.append([s,[s]])
    while q:
        node,path=q.pop(0)

        if node==d:
            result.append(path.copy())
            continue
        for child in  graph[node]:
            if child not in path:
                newpath=path+[child]
                q.append([child,newpath])
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