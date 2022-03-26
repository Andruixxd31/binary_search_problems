'''
My Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, node):

        p = node
        c = 1
        while node:
            if node.next and c:
                node.val, node.next.val = node.next.val, node.val
                c = 0
            else:
                c = 1
            node = node.next

        return p
