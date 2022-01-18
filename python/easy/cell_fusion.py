'''
My solution
Time: O(nlogn)
Space: O(n)
'''

class Solution:
    def solve(self, cells):
        cells = [-n for n in cells]
        heapq.heapify(cells)
        while len(cells) > 1:
            a = heapq.heappop(cells)
            b = heapq.heappop(cells)
            if a != b:
                heapq.heappush(cells, math.ceil((a+b)/3))

        return -cells.pop() if len(cells) == 1 else -1
