from collections import defaultdict


def topological_sort_dfs(graph):
    # Create adjacency list representation if not already in that form
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    # Set to track visited nodes
    visited = set()
    # List to store the topological order
    result = []

    def dfs(node):
        visited.add(node)
        # Explore all neighbors (dependencies)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor)
        # Add node to result after all dependencies are processed
        result.append(node)

    # Process all nodes to handle disconnected components
    for node in set([u for u, v in graph] + [v for u, v in graph]):
        if node not in visited:
            dfs(node)

    # Reverse the result to get the correct topological order
    return result[::-1]


# Example usage
graph = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
# Represents: 5->2, 5->0, 4->0, 4->1, 2->3, 3->1
result = topological_sort_dfs(graph)
print(result)  # Possible output: [5, 4, 2, 3, 1, 0]