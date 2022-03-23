'''
My Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, s):
        dic = Counter(s)
        odd = 0
        for val in dic:
            if dic[val]%2 != 0:
                odd += 1
        
        return True if odd <= 1 else False

