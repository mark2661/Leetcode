# import heapq
#
#
# class charObject:
#     def __init__(self,val,frequency):
#         self.val = val
#         self.frequency = frequency
#
#     def __eq__(self, other):
#         return self.frequency == other.frequency
#
#     def __gt__(self, other):
#         return self.frequency > other.frequency
#
#     def __lt__(self, other):
#         return self.frequency < other.frequency
#
#
# class Solution:
#     def frequencySort(self, s):
#         self.ft = dict()
#         self.ob = []
#         self.result = ""
#         heapq.heapify(self.ob)
#
#         for c in s:
#             if c in self.ft:
#                 self.ft[c] += 1
#             else:
#                 self.ft[c] = 1
#
#         for k,v in self.ft.items():
#             heapq.heappush(self.ob, charObject(k,-v))
#
#         while self.ob:
#             c = heapq.heappop(self.ob)
#             self.result += c.val * (-1 * c.frequency)
#         return self.result

import heapq

class Solution:
    def frequencySort(self, s):
        self.ft = dict()
        self.ob = []
        self.result = ""
        heapq.heapify(self.ob)

        for c in s:
            if c in self.ft:
                self.ft[c] += 1
            else:
                self.ft[c] = 1

        for k,v in self.ft.items():
            heapq.heappush(self.ob, (-v,k))

        while self.ob:
            v,k = heapq.heappop(self.ob)
            self.result += k * (-1 * v)
        return self.result

