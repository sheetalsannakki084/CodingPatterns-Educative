


def solution(nums,new):
    result=[]

    for i in range(len(nums)):
        if new[1]<nums[i][0]:
            result.append(new)
            return result+nums[i:]
        elif nums[i][1] < new[0]:
            result.append(nums[i])
        else:
           new=([min(nums[i][0],new[0]),max(nums[i][1],new[1])])




    return result
    





input=[[3,4],[5,7],[9,10]]
new=[1,2]
obj=solution(input,new)
print(obj)