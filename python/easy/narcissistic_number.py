'''
My Solution
Time: O(logn)
Space: O(1)
'''

class Solution:
    def solve(self, n):
        res = 0
        c = 1
        m = k = n
        while m >= 10:
            m //= 10
            c += 1
        
        while k > 0:
            res += math.pow(k%10, c)
            k //= 10

        return n == res

