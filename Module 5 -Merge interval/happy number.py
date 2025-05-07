
def solution(n):


    def sqrtsum(n):
        sum = 0
        while n >0:
            digit=n%10
            n=n//10
            sum+=digit**2
        return sum


    slow=n
    fast=sqrtsum(n)
    while fast!=1 and slow !=fast:
        slow=sqrtsum(slow)
        fast=sqrtsum(sqrtsum(fast))
    if fast==1:
        return True
    return False





n=2
obj=solution(n)
print(obj)