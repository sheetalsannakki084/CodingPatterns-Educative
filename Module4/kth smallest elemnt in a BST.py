import heapq

#kth smallest element so we used maxheap
# def solution(input,k):
#     minheap=[]
#     heapq.heapify(minheap)
#
#     for num in input:
#         heapq.heappush(minheap,-num)
#         if len(minheap)>k:
#             heapq.heappop(minheap)
#
#     return -1*minheap[0]


#kth largest element so we used minheap
def solution(input,k):
    minheap=[]
    heapq.heapify(minheap)

    for num in input:
        heapq.heappush(minheap,num)
        if len(minheap)>k:
            heapq.heappop(minheap)

    return minheap[0]












input=[1,4,6,5,3,2]
k=2
obj=solution(input,k)
print(f"{k} nd largest element in this {input} is",obj)