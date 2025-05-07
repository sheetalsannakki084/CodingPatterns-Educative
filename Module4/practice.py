import heapq


class solution:
    def __init__(self):
        self.minheap=[]
        self.maxheap=[]

    def insert(self,num):
        if not self.maxheap or -self.maxheap[0]>=num:
            heapq.heappush(self.maxheap,-num)

        else:
            heapq.heappush(self.minheap,num)


        if len(self.maxheap)>len(self.minheap)+1:
            heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))
        elif len(self.maxheap)<len(self.minheap):
            heapq.heappush(self.maxheap,-heapq.heappop(self.minheap))

    def findmedian(self):

        if len(self.maxheap)==len(self.minheap):
            return (-self.maxheap[0]+self.minheap[0])/2.0

        return -self.maxheap[0]




input=[35, 22,30,25]
obj=solution()

for num in input:
    i=obj.insert(num)

print(obj.findmedian())