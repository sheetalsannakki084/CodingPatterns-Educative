

def solution(n):
    s=sorted(n)
    l=0
    r=len(s)-1
    t=79
    while l<=r:
        mid=(l+r)//2
        if s[mid]==t:
            return mid
        elif s[mid]<t:
            l = mid + 1
        else:
            r=mid-1
    return -1




nums=-3,5,34,78,33,1,45
obj=solution(nums)
print(obj)