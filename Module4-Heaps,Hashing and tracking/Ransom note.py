import collections


def solution(ran,mag):
    table1=collections.Counter(mag)




    for i in ran:
        if i in table1:
            table1[i]-=1
        else:
            return False

    return True


  # for i in ran:
  #       if i not in table1 or table1[i]==0:
  #           return False
# this also works and same as above but edge case







ran="program"
mag="rpgoam"
result=solution(ran,mag)
print(result)