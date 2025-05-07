

def solution(nums):
    l=0
    r=len(nums)-1
    t=7
    while l<=r:
        mid=l+(r-l)//2
        if nums[mid]==t:
            return mid
        if nums[l]<=nums[mid]:
            if nums[l]<=t and t<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        else:
             if nums[r]>=t and t>nums[mid]:
                 l=mid+1
             else:
                 r=mid-1

    return -1



nums=6,7,1,2,3,4,5
obj=solution(nums)
print(obj)