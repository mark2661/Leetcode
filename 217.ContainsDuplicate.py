class Solution:
    def containsDuplicate(self, nums):
        hs = set()
        for n in nums:
            if n in hs:
                return True
            hs.add(n)
        return False
