def solution(nums):
    result=[]
    sum=0



    for num in nums:
        sum+=(num*2)
        result.append(sum)
        n=sum
    return result

    # sum=0
    # prefix=[]
    # for n in result:
    #     sum+=n
    #     prefix.append(sum)
    #     n=sum


    # return prefix












nums=[2,3,7,5,10]
result=solution(nums)

print(result)