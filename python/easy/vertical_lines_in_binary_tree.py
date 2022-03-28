'''
My Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, root):
        pos = set()
        self.traverse(root, 0, pos)
        return(len(pos))
    
    def traverse(self, node, line, pos):
        pos.add(line)
        
        if node.left:
            self.traverse(node.left, line-1, pos)
        if node.right:
            self.traverse(node.right, line+1, pos)
    
