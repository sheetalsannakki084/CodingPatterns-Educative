

def solution(w):
    n=3
    count=0
    ws=sorted(w)
    l=0
    r=len(ws)-1
    while l<=r:
        if ws[l]+ws[r]<=n:
            count+=1
            l+=1
            r-=1
        else:
            r-=1
            count+=1

    return count










w=[1,2]
obj=solution(w)
print(obj)