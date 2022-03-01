'''
My Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, node):
        c = 0
        while node is not None:
            c += 1
            node = node.next
        return(c)
