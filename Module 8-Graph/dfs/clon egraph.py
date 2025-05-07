

def solution(graph):
    visited={}
    n=len(graph)

    def dfs(node):
        if node in visited:
            return node

        visited[node]=[]
        nodex=node-1

        for child in graph[nodex]:
            visited[node].append(dfs(child))
        return node

    dfs(1)

    result=[[] for _ in range(n)]
    for node in visited:
        result[node-1]=visited[node]
    return result







graph= [[2,4],[1,3],[2,4],[1,3]]
cloned = solution(graph)
print(cloned)