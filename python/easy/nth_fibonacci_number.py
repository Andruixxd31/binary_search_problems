'''
My Solution
Time: O(n)
Space: O(n)
'''
class Solution:
    def solve(self, n):
        l = [0] * n
        for i in range(min(2,n)):
            l[i] = 1
        
        for i in range(2, n):
            l[i] = l[i-1] + l[i-2]
       
        return(l[n-1]) if n > 0 else 1
