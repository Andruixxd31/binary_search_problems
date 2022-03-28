'''
My Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, nums):
        s = set(nums)

        c = 1
        for i in s:
            if c not in s: return c
            c += 1
        return c
