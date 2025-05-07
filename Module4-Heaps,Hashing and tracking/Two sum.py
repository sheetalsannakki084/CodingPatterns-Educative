

def solution(arr,t):
    table={}



    for i in range(len(arr)):
        d=t-arr[i]
        if d not in table:
            table[arr[i]]=i
        else:
            return i,table[d]










arr=[-2,2,11,15,-3]
t=8
result=solution(arr,t)
print(result)