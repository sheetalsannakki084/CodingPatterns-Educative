

def solution(col):
    l=0
    n=len(col)
    r=n-1
    maxarea=0
    while l<r:
        h=min(col[l],col[r])
        area=h*(r-l)
        maxarea=max(area,maxarea)
        if col[l]<=col[r]:
            l+=1
        else:
            r-=1
    return maxarea











col=[8,2,6,3,5,4,7]
obj=solution(col)
print("maxarea is",obj)
