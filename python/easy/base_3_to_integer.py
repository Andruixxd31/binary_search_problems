
#My solution
Class Solution:
    def solve(self, s):
        s = s[::-1] #copies string, uses memory
        total = 0
        for i in range(len(s)): #could use reverse an an extra var to use O(1) memory
            total += (3**i) * int(s[i])
        return total
