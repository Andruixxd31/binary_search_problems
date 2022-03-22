'''
My solution
Time: O(n)
Space: O(1)
'''

class Solution:
    def solve(self, moves, x, y):
        currX, currY = 0, 0
        d = {
            "EAST": (1, 0),
            "WEST": (-1, 0),
            "NORTH": (0, 1),
            "SOUTH": (0, -1),
        }
        for i in moves:
            dx, dy = d[i]
            currX += dx
            currY += dy
        return currX == x and currY == y
