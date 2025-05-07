import collections


def solution(task,n):
    table=collections.Counter(task)


    sorttable=sorted(table.values(),reverse=True)
    maxfrq=sorttable[0]

    time=(maxfrq-1) * n
    for frq in sorttable[1:]:
        time=time-min(maxfrq-1,frq)
    time=max(0,time)

    return len(task)+time

# solve using this frfmula undertsand


task=['A', 'A', 'B','B','A']
n=2
obj =solution(task,n)
print(obj)