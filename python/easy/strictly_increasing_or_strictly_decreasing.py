'''
My Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, nums):
        asc = True
        desc = True

        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                desc = False
            if nums[i-1] <= nums[i]:
                asc = False
        
        return asc or desc
