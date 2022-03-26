'''
My Solution
time: O(n²logn)
Space: O(1)
'''

class Solution:
    def solve(self, nums, k):
        nums.sort()

        
        for i in range(len(nums)):
            c = i
            l = c +1
            r = len(nums) -1
            while l < r:
                a = nums[c] + nums[l] + nums[r]
                if a == k:
                    return True
                elif a < k:
                    l += 1
                else:
                    r -= 1
        return False

'''
Other Solution
Time: O(n²)
Space: O(n)
'''

class Solution:
    def solve(self, nums, k):
        s = set()
        for i in range(len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if k - (nums[i] + nums[j]) in s:
                    return True
            s.add(nums[i])
        return False
