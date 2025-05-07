import heapq

minheap = []
print("minheap is")
heapq.heappush(minheap, 2)
heapq.heappush(minheap, 8)
heapq.heappush(minheap, 4)
heapq.heappush(minheap, 1)

while len(minheap):
    print(heapq.heappop(minheap))



maxheap=[]
print("max heap is")
heapq.heappush(maxheap,-10)
heapq.heappush(maxheap,-2)
heapq.heappush(maxheap,-4)
heapq.heappush(maxheap,-8)

while len(maxheap):
    print(-1*heapq.heappop(maxheap))
