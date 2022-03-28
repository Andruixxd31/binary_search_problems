'''
My Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, root, target):
        if target < 1: return False
        
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.val == target:
                return True
            if node.val > target:
                return False
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
