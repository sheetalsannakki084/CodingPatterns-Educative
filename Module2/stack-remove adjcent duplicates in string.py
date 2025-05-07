
def solution(ans):
    stack=[]

    for k in ans:
        if stack and stack[-1]==k:
            stack.pop()
        else:
            stack.append(k)
    return stack





ans=['a','b','b','a','a','c','a']
obj=solution(ans)
print(obj)