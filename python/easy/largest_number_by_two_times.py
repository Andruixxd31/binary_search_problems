'''
My Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, nums):
        n = m = -math.inf
        for num in nums:
            if n < num:
                m = n
                n = num
            elif m < num:
                m = num
        return n > m*2
