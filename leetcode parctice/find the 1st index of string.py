def strStr(haystack, needle):
    if not needle:
        return 0  # If needle is empty, return 0 (per the problem description)

    # We only need to check the length of haystack and needle to prevent index out of range
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i  # If a match is found, return the starting index
    return -1  # If no match is found, return -1


haystack = "sadbutsad"
needle = 'said'
obj = strStr(haystack, needle)
print(obj)
