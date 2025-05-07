import heapq

class Solution:
    def __init__(self):
        self.minheap = []  # To store the larger half of numbers
        self.maxheap = []  # To store the smaller half of numbers (in negative for max-heap behavior)

    def insert(self, num):
        # Insert into max-heap or min-heap based on the value
        if not self.maxheap or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)  # We store negative values to simulate max-heap
        else:
            heapq.heappush(self.minheap, num)

        # Balance the heaps: if one heap has more than one extra element, move the top of that heap
        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        elif len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findmedian(self):
        # If the heaps are balanced in size, the median is the average of the top elements of both heaps
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2.0
        # If the heaps are unbalanced, the median is the top of the max-heap
        return -self.maxheap[0]

# Input
nums = [30, 22,35,25,15]
obj = Solution()

# Insert each element from the list into the object
for num in nums:
    obj.insert(num)

# Output the median after all insertions
print(obj.findmedian())

#max-35 min=[]
# next22 add 35,22
# no balance so pop 35 ans add to minheap.max=22  min=35 next 30 now 22>30 no so add to minheap 30,35
# balance nt dr so pop minheap[0] add to maxheap max=30,22  min=35
# next add 25 which leass den maxheap[0] so add to maxheap,30,22,25
# no balance pop 30 and to minheap so max=25,22 min=30,35
# equal length so 25+30=55/2=27.5


