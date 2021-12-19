
def sumQ(arr,left,right,memo = dict()):
    if "{0},{1}".format(left,right) in memo:
        return memo["{0},{1}".format(left,right)]
    if left == right:
        return arr[left]
    memo["{0},{1}".format(left,right)] = arr[left] + sumQ(arr,left + 1, right, memo)
    return memo["{0},{1}".format(left,right)]


class NumArray:

    def __init__(self, nums, memo = dict()):
        self.nums = nums
        self.memo = memo


    def sumRange(self, left, right):
        return sumQ(self.nums,left,right,self.memo)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# obj = NumArray([-2,0,3,-5,2,-1])
# print(obj.sumRange(0,2))
# print(obj.sumRange(2,5))
# print(obj.sumRange(0,5))
obj = NumArray([1,4,-6])
print(obj.sumRange(0,2))
print(obj.sumRange(1,2))
print(obj.sumRange(0,1))
