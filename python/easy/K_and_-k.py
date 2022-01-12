'''
my solution
Time O(n)
Space O(n)
'''
class Solution:
    def solve(self, nums):
        s = set(nums)
        res = -1
        for n in nums:
            if -n in s:
                ans = max(ans, abs(n))
        return res
                
