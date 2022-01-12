'''
My Solution
Time: O(n)
Space: O(n)
'''
class Solution:
    def solve(self, nums):
        d = {}
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = -1
            else:
                d[num] = i

        res = [x for i,x in enumerate(nums) if i != d[x]]
        return res
