'''
My Solution
Time: O(n)
Space: O(n)
'''
class Solution:
    def checklen(self, num, n):
        if num // (10**n) == 0:
            return n
        else:
            return self.checklen(num, n+1)
    
    def solve(self, num):
        left = self.checklen(num, 0) - 1
        right = 0 
        while left > right:
            if num // 10**left %10 == num // 10**right % 10:
                left -= 1
                right += 1
            else:
                return False
        return True

'''
Other Solution
Time: O(logn)
Space: O(n)
'''

class Solution:
    def solve(self, num):
        a = 0
        c = num
        while num > 0:
            r = num % 10
            num = num // 10
            a = (10 * a) + r
        if a == c:
            return True
        else:
            return False
