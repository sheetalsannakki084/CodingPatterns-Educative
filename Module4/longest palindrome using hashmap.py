

def solution(ans):
    table={}
    for i in ans:
        if i in table:
            table[i]+=1
        else:
            table[i]=1


    length=0


    for count in table.values():
        length+=(count//2)*2


    if length<len(ans):
        length+=1


    return length



ans='aabcaaa'
result=solution(ans)
print(result)