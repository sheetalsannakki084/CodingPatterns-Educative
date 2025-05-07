

def solution(col):
    n=len(col)-1
    s,c,end=0,0,n
    while c<=end:
        if col[c]==0:
            col[s],col[c]=col[c],col[s]
            c+=1
            s+=1
        elif col[c]==1:
            c+=1
        else:
            col[c],col[end]=col[end],col[c]
            end-=1
    return col



col=[0,1,1,2,0,2,0,2,1,2]
obj=solution(col)
print(obj)