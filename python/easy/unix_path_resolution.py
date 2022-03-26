'''
My Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, path):
        st = []
        for d in path:
            if d != ".." and d != ".":
                st.append(d)
            elif d == ".." and st:
                st.pop()
        return st
