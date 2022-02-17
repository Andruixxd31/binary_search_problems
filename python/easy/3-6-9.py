'''
My Solution
Time: O(NlogN)
Space: O(n)
'''

class Solution:
    def solve(self, n):
        l = []
        for i in range(n):
            a = i + 1
            if a % 3 == 0:
                l.append("clap")
                continue
            while a > 0: 
                if a % 10 in [3,6,9]:
                    l.append("clap")
                    break
                else:
                    a = a // 10
            if a == 0: 
                l.append(str(i+1))

        return l

'''
Other Solution
'''

class Solution:
    def solve(self, n):
        def valid(x):
            if x % 3 == 0:
                return False
            while x:
                if x % 10 in [3, 6, 9]:
                    return False
                x //= 10
            return True

        return [str(i) if valid(i) else "clap" for i in range(1, n + 1)]
