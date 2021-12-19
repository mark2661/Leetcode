import heapq


class Solution:
    def sortArray(self, nums):
        self.q = nums
        self.result = []
        heapq.heapify(self.q)
        while self.q:
            self.result.append(heapq.heappop(self.q))
        return self.result

