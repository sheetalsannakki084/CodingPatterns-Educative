
def solution(num):
    numsort=sorted(num)
    t=18
    sum=0
    n=len(numsort)
  # ALL NUMBER SSHD BE DIFF SO l<r and i not queal to l or so i ends with n-2
    for i in range(0,n-2):
        l = i + 1
        r = n - 1
        while l<r:
            sum = numsort[i] + numsort[l] + numsort[r]
            if sum == t:
                return True
            elif sum < t:
                l += 1
            else:
                r -= 1
    return False

num=[2, 3, 4, 1, 7, 9]

obj=solution(num)
if obj:
    print("sum exist")
else:
    print("not exist")
