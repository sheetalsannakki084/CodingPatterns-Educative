


def solution(ar,k):

    l=0
    r=0
    sum=0
    maxsum=0

    while r<len(ar):
        if (r-l+1)<=k:
            sum+=ar[r]
            r+=1
            maxsum=max(maxsum,sum)
        else:
            sum=0
            l+=1
            r=l
    return maxsum









arr=[1, 4, 2, 10, 2, 3, 1, 0, 20]
k=4
obj=solution(arr,k)
print(obj)