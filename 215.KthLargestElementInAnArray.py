import heapq

class Solution:
    def findKthLargest(self, nums, k):
        self.q = [-1*n for n in nums]
        heapq.heapify(self.q)
        for i in range(k):
            val = heapq.heappop(self.q) * -1
        return val


