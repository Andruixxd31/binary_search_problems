'''
My solution:
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, nums, k):
        s = set()
        for num in nums:
            if k - num in s:
                return True
            s.add(num)
        return False
