'''
My Solution
Using KMP algorithm 
Time: O(n * m)
Space: O(n + m)
'''


class Solution:
    def solve(self, needle, haystack):
            if len(needle) != len(haystack): return False
            lps = [0] * len(needle)
            
            prevLPS, i = 0, 1
            while i < len(needle):
                if needle[i] == needle[prevLPS]:
                    lps[i] = prevLPS + 1
                    prevLPS += 1
                    i += 1
                elif prevLPS == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prevLPS = lps[prevLPS - 1]

            i = 0
            j = 0 

            haystack *= 2
            while i < len(haystack):
                if haystack[i] == needle[j]:
                    i, j = i + 1, j + 1
                else:
                    if j == 0:
                        i += 1
                    else:
                        j = lps[j - 1]
                if j == len(needle):
                    return True
            return False
        
'''
My Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, s0, s1):
        if len(s0) != len(s1):
            return False
        s0 = s0 + s0
        return True if s0.find(s1) != -1 else False
