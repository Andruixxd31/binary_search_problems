'''
My Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, rooms, target):
        for val in rooms:
            if val >= target: return val
        return -1
