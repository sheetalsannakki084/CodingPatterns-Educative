def solution(num):
    b=0
    s=1
    count=0

    while s<len(num):
        sum = num[s] - num[b]
        if num[b]<num[s]:
            count=max(count,sum)
        else:
            b=s

        s+=1

    return count










input=[8,2,6,4,7,5]
obj=solution(input)
print(obj)