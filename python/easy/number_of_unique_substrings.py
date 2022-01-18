'''
My Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, s):
        tmp = 0
        ll = s[0] if len(s) > 0 else ' '
        total = 0
        for l in s:
            if l != ll:
                total += tmp * (tmp + 1) / 2
                ll = l
                tmp = 1
            else:
                tmp += 1

        total += tmp * (tmp + 1) / 2
        return total
