'''
My Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, intervals, point):
        accum = 0
        for x, y in intervals:
            if x <= point and point <= y: accum += 1
        return accum
'''
Other Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, intervals, point):
        return sum(a <= point and point <= b for a, b in intervals)

