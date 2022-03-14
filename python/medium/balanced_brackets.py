'''
My Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, s):
        balance = 0
        for char in s:
            if char == '(': balance += 1
            else: balance -= 1
            if balance < 0: break
    
        return True if balance == 0 else False


