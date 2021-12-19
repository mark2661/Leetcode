from bisect import bisect_left, bisect_right

class Solution:
    def findClosestElements(self, arr, k, x):
        if len(arr) == k:
            return  arr
        x_idx = bisect_right(arr, x)
        if 0 < x_idx < len(arr):
            back = x_idx if abs(arr[x_idx] - x) < abs(arr[x_idx - 1] - x) else x_idx - 1
        else:
            back = x_idx
        front = back
        print(x_idx,back,front)

        while front - back - 1 < k:

            if back == -1:
                front += 1
                continue

            if front == len(arr) or abs(arr[back] - x) <= abs(arr[front] - x):

                back -= 1
            else:
                front += 1

        return arr[back + 1:front]


my_solution = Solution()
#print(my_solution.findClosestElements([1,2,3,4,5],4,3))
#print(my_solution.findClosestElements([1,2,3,4,5],4,-1))
#print(my_solution.findClosestElements([-2,-1,0,1,2,3,4,5],7,3))
print(my_solution.findClosestElements([0,0,1,2,3,3,4,7,7,8],3,5))
#print(my_solution.findClosestElements([-2,-1,1,2,3,4,5],7,3))
