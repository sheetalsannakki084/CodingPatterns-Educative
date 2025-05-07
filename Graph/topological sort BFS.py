from collections import defaultdict, deque


def topological_sort_bfs(graph):
    # Create adjacency list and in-degree count
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)

    # Build the graph and compute in-degrees
    all_nodes = set()
    for u, v in graph:
        adj_list[u].append(v)
        in_degree[v] += 1
        all_nodes.add(u)
        all_nodes.add(v)

    # Initialize queue with nodes having in-degree 0
    queue = deque([node for node in all_nodes if in_degree[node] == 0])
    result = []

    # Process nodes
    while queue:
        node = queue.popleft()
        result.append(node)

        # Reduce in-degree of neighbors
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycle
    if len(result) != len(all_nodes):
        return None  # Indicates a cycle exists

    return result

graph = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
# Represents: 5->2, 5->0, 4->0, 4->1, 2->3, 3->1
result = topological_sort_bfs(graph)
print(result)