'''
My Solution
Time: O(1)
Space: O(1)
'''

class Solution:
    def solve(self, n):
        while n > 9:
            total = 0
            while n > 0:
                total += n % 10
                n = n // 10
            n = total
        return n

'''
Other Solution
Time: O(1)
Space: O(1)
'''

class Solution:
    def summ(self, n):
        sol = 0
        while n > 0:
            sol += n % 10
            n = n // 10
        return sol

    def solve(self, n):
        if n < 10:
            return n
        n = self.summ(n)
        return self.solve(n)


