def solution(arr,k):
    l,r=0,0
    result=[]
    output=[]


    while r<len(arr):
        if (r-l+1)<=k:
           result.append(arr[r])
           r+=1


        if (r-l+1)>k:
            output.append(max(result))
            l+=1
            r=l
            result=[]

    return output








arr=[5,1,3,4,2,6,]
k=1
obj=solution(arr,k)
print(obj)