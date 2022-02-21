'''
My Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, s):
        unique = set()
        for char in s:
            if char not in unique:
                unique.add(char)
            else:   return False
        return True

'''
Other Solution
Time: O(n)
Space: O(1)
'''


class Solution:
    def solve(self, s):
        chars = 0
        for char in s:
            char_i = ord(char) - 97
            if chars & (1 << char_i):
                return False
            chars += 1 << char_i
        return True


