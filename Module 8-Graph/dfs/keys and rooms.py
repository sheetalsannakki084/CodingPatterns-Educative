
def dfs(rooms):
    visited=set()
    def dfs(s):
        if s not in visited:
            visited.add(s)
            for child in rooms[s]:
                dfs(child)

    dfs(0)
    return len(visited)==len(rooms)








rooms=[[1,3],[3,0,1],[2],[0]]
obj=dfs(rooms)
print(obj)

