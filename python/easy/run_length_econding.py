'''
My Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, s):
        encode = ""
        n = 0
        current = s[0]
        for c in s:
            if c == current:
                n +=1
            else:
                encode += str(n) + current
                n = 1
                current = c
        return encode
