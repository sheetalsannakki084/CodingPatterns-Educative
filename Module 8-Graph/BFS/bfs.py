
def solution(s):
    visited=set()

    queue=[]
    queue.append(s)
    while queue:
        node=queue.pop(0) #pop frm front
        print(node)
        visited.add(node)

        for child in graph[node]:
            if child not in visited:
                queue.append(child)
                visited.add(child)








graph={
    "a":["c","b"],
    "b":['a','d'],
    "c":['a'],
    "d":["b","e","f"],
    "e":["d"],
    "f":["d","g"],
    "g":["f"]}
s="a"
obj=solution(s)
