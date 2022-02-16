'''
My Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, prices):
        l = 0
        md = 0
        for i, h in enumerate(prices) :
            if prices[l] < h:
                dif = abs(prices[l] - h)
                if dif > md: md = dif
            else:
                l = i
        return md
