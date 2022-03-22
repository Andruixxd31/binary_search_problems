'''
Recursive Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, n):
        return self.factorial(n)

    def factorial(self, n):
        if n == 1: return 1
        else: return n*factorial(n-1)

'''
Iterative Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, n):
        if n == 0:
            return 1
        res = n
        while n != 1:
            n = n - 1
            res = res * n
        return res
