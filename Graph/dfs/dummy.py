from collections import defaultdict


def solution(graph):

    mat=defaultdict(list)

    for u,v in graph:
        mat[u].append(v)

    visited=set()
    result=[]


    def dfs(node):
        visited.add(node)

        for child in mat[node]:
            if child not in visited:
                dfs(child)

        result.append(node)

    for node in set([u for u,v in graph]+[v for u,v in graph]):
        if node not in visited:
            dfs(node)


    return result[::-1]























graph = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
obj=solution(graph)
print(obj)