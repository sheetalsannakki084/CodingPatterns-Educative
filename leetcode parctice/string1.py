import collections


def solution(s):
    table = collections.Counter(s)

    all_val = table.values()
    print(len(set(all_val)))
    return len(set(all_val)) == 1













s='abcbc'
obj=solution(s)
print(obj)