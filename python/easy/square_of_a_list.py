'''
My Solution
Time: O(nlogn)
Space: O(n)
'''

class Solution:
    def solve(self, nums):
        return sorted([x ** 2 for x in nums])

'''
Other Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, nums):
        n = len(nums)
        l = 0
        r = n - 1
        index = n - 1
        res = [0 for i in range(len(nums))]
        while index >= 0:
            if abs(nums[l]) > abs(nums[r]):
                res[index] = nums[l] * nums[l]
                l += 1
            else:
                res[index] = nums[r] * nums[r]
                r -= 1
            index -= 1

        return res


