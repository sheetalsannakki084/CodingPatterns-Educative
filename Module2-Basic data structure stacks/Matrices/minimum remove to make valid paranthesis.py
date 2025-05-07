

def solution(m):
    stack=[]
    s=list(m)
    for i , e in enumerate(s):
        if stack and stack[-1][0]=="(" and e ==')':
            stack.pop()
        elif e==')' or e=='(':
            stack.append([e,i])

    for k in stack:
        s[k[1]]= ""

    result = ''.join(s)

    return result




m="a)di(o)qw("
obj=solution(m)
print(obj)