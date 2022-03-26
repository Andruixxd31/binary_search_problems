'''
My Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, node):
        tmp = node
        while node:
            node.next = self.changeP(node, node.val)
            node = node.next
    
        return tmp
    
    def changeP(self, node, jumps):
        if not node:
            return None

        if jumps == 0:
            return node
        else:
            return self.changeP(node.next, jumps-1)


'''
Iterative Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, node):
        if not node:
            return None

        curr = node
        while curr:
            jump = curr.val
            j = curr

            while jump > 0 and j:
                j = j.next
                jump -= 1

            curr.next = j
            curr = curr.next

        return node
