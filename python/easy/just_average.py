#My first Solution
'''
Uses O(n) memory and in time is O(n)
'''
class Solution:
    def solve(self, nums, k):
        dic = {}
        total = 0
        for n in nums:
            total += n
            dic[n] = n
        dt = k*(len(nums)-1)
        if (total - dt) in dic:
            return True
        return False

#Other solution
'''
memory O(1) time -> O(2n) = O(n)
'''
class Solution:
    def solve(self, nums, k):
        return sum(nums) - k * (len(nums) - 1) in nums
