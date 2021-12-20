'''
My solution
Time: O(n+m)
Space: O(n+m)
'''

class Solution:
    def solve(self, a, b):
        if not a: return b
        if not b: return a
        c = []
        i = j = 0
        for n in range(len(a) + len(b)):
            if a[i] <= b[j]:
                c.append(a[i])
                i += 1
                if i == len(a):
                    c += b[j:]
                    break
            else:
                c.append(b[j])
                j += 1
                if j == len(b):
                    c += a[i:]
                    break
        return c

'''
Better Solution:
Time: O(n)
Space: O(n)
'''
def solve(self, l, r):
        li, ri, result = 0, 0, []
        while li < len(l) and ri < len(r):
            if l[li] <= r[ri]:
                result.append(l[li])
                li += 1
            else:
                result.append(r[ri])
                ri += 1

        return result + l[li:] + r[ri:]
