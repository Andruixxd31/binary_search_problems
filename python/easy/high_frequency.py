'''
My Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, nums):
        count = Counter(nums)
        mx = 0
        for k in count:
            mx =max(mx, count[k])
        return mx


'''
Other Solution
Time: O(n)
Space: O(n)
'''

class Solution:
    def solve(self, nums):
        return Counter(nums).most_common(1)[0][1] if nums else 0
