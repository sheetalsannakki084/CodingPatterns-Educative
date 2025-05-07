import heapq


# def solution(input,k):
#     result=[]
#     value=float("inf")
#
#     for x,y in input:
#         if k>0:
#             sum=x**2 +y**2
#             if sum<value:
#                 k-=1
#                 value=sum
#                 result.append([x,y])
#     return result

def solution(input,k):
    minheap=[]
    for x,y in input:
        dist=(x**2) +(y**2)
        minheap.append([dist,x,y])

    heapq.heapify(minheap)
    res=[]
    while k>0:
        dist,x,y=heapq.heappop(minheap)
        res.append([x,y])
        k-=1
    return res





input=[(-1, -3),(-4, -5),(-2, -2),(-2, -3)]
k=3
obj=solution(input,k)
print("smallest is",obj)