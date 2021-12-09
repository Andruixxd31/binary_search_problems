'''
My Solution
Space: O(1)
Time: O(n)
'''
class Solution:
    def solve(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].islower():
                i += 1
                continue
            if not s[j].islower():
                j -=1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
