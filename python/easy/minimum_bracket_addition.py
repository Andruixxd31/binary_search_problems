'''
My Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, s):
        op, cl = 0, 0
        for char in s:
            if char == '(':  
                op += 1
            elif op:
                op -= 1
            else:
                cl += 1
        
        return op + cl
