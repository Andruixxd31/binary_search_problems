'''
My solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, words):
        csl = msl = 0
        ll = ' '
        for word in words:
            if word[0] == ll:
                csl += 1
            else:
                ll = word[0]
                csl = 1
            
            if csl > msl: msl = csl
        
        return msl
