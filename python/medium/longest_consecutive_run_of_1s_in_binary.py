'''
My Solution
Time: O(logn)
Space: O(1)
'''

class Solution:
    def solve(self, n):
        mx = tmpmx = 0
        st = 1
        while st <= n:
            if (n & st) > 0:
                tmpmx += 1
            else:
                tmpmx = 0
            if tmpmx > mx:
                mx = tmpmx
            st *= 2 
            
        return mx

'''
Other Solution
Time: O(logn)
Space: O(1)
'''

class Solution:
    def solve(self, n):

        ## initialise count = 0
        count = 0

        # Count the number of iterations to reach n=0
        while n != 0:

            # This operation reduces length of every sequence of 1s by one.
            n = n & (n << 1)

            count = count + 1

        return count
