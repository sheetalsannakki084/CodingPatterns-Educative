

def solution(rooms):
    visited=set()

    def bfs(s):

        q = [s]
        visited.add(s)
        while q:
            node = q.pop(0)

            for child in rooms[node]:
                if child not in visited:
                    q.append(child)
                    visited.add(child)

    bfs(0)
    return len(visited)==len(rooms)




rooms=[[1],[2],[3],[]]
obj=solution(rooms)
print(obj)

