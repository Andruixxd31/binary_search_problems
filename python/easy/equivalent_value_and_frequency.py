'''
My Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, nums):
        d = Counter(nums)
        return any(k == v for k, v in d.items())
