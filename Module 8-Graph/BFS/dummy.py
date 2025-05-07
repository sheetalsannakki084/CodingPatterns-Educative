p1 = {"hacker": "rank", "input": "output"}
p2 = {"hacker": "ranked", "input": "wrong"}

# Find the keys where the values differ
diff_keys = [key for key in p1 if p1[key] != p2.get(key, None)]

# Sort the keys alphabetically
sorted_diff_keys = sorted(diff_keys)

# Print the result
print(sorted_diff_keys)
