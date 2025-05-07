
def solution(a,b):
    table={}

    for i in range(len(a)):
        if a[i] not in table:
            table[a[i]]=i

        return table

    result = []
    for j in b:
        if j in table:
            result.append(i)

    return min(result)










a="abcbac"
b="abc"
result=solution(a,b)
print(result)