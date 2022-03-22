'''
My Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, n):
        res = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                res.append("FizzBuzz")
            elif i%3 == 0:
                res.append("Fizz")
            elif i%5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res

'''
Other Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, n):
        return [
            "FizzBuzz" if not i % 15 else "Buzz" if not i % 5 else "Fizz" if not i % 3 else str(i)
            for i in range(1, n + 1)
        ]
