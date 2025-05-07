from collections import defaultdict


def restoreArray(adjacentPairs):
  graph = defaultdict(list)

  for x, y in adjacentPairs:
    graph[x].append(y)
    graph[y].append(x)

  root = None
  for num in graph:
    if len(graph[num]) == 1:
      root = num
      break

  def dfs(node, vis, res):

    res.append(node)
    vis.add(node)

    for neighbor in graph[node]:
      if neighbor not in vis:
        dfs(neighbor, vis, res)

  res = []
  vis = set()
  dfs(root,vis,res)
  return res




s=[[4,-2],[1,4],[-3,1]]
obj=restoreArray(s)
print(obj)