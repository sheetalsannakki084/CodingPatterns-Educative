import collections


def solution(nums):
    table=collections.Counter(nums)


    return max(table.keys(),key=table.get)
#  or u can write using lambda

# return max(table.keys(),key=lambda x:table[x])
#
# #
# or bewlo code
# def solution(nums):
#     table = collections.Counter(nums)
#     max_key = None
#     max_count = -1
#     for key in table:
#         if table[key] > max_count:
#             max_count = table[key]
#             max_key = key
#     return max_key


# for key, value in records.items(): ofr both values key n value
#     print(f"Element {key} has frequency {value}")

# for value in table.values()
# for key in table.key()




nums=[2, 2, 3, 2, 2, 1, 2, 3,3,3,3,3,3,3]
result=solution(nums)

print(result)