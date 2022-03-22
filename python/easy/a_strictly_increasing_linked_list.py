'''
My Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, head):
        while head.next:
            if head.val >= head.next.val: return False
            head = head.next
        return True
