'''
My Solution
Time O(n)
Space: O(1)
'''

class Solution:
    def solve(self, node):
        
        tmp = node
        c = total = 0
        while tmp:
            c += 1
            tmp = tmp.next
        
        while node:
            if node.val == 1:
                total += math.pow(2, c-1)
            node = node.next
            c -= 1
        return total

'''
Other Solution
Time: O(n)
Space: O(1)
'''
class Solution:
    def solve(self, node):
        a = ""
        while node:
            a+=str(node.val)
            node = node.next
        return int(a,2)

'''
Third Solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, node):
        num = 0
        while node:
            num <<= 1
            # print(num)
            num += node.val
            node = node.next
        return num
