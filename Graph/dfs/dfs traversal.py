def solution(graph,s):
    visited=set()
    stack=[]

    stack.append(s)
    while stack:
        node=stack.pop()

        if node not in visited:
            visited.add(node)
            print(node)

            for child in graph[node]:
                if child not in visited:
                    stack.append(child)

# without satck recursive
# def solution(graph, s):
#     visited = set()
#
#     def dfs(node):
#         visited.add(node)
#         print(node)
#
#         for child in graph[node]:
#             if child not in visited:
#                 dfs(child)
#
#     dfs(s)


graph={
    "a":["c","b"],
    "b":['a','d'],
    "c":['a'],
    "d":["b","e","f"],
    "e":["d"],
    "f":["d","g"],
    "g":["f"]}

s="a"
obj=solution(graph,s)
print(obj)
# bfs
# Start from "a", visit "b" and "c".
# Then visit "b"'s neighbors "d" and "e".
# Visit "c"'s neighbor "f".
# Visit "d"'s neighbor "g".
# Finally, visit "f"'s neighbor "h".
#
# dfs satck=a
# pop a den s=b,c pop c den its child append stack
# Start at "a", then visit "c", then "f", then "h".
# After that, backtrack to "b", visit "b"'s neighbors "e" and "d", and finally visit "d"'s neighbor "g".