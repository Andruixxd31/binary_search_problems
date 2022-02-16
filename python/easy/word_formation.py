'''
My Solution
Time: O(n * m)
Space: O(m)
'''

class Solution:
    def solve(self, words, letters):
        dic = {}
        for letter in letters:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        
        longest = 0
        for word in words:
            dic_cop = dic.copy()
            is_match = True
            if len(word) > longest:
                for l in word:
                    if l in dic_cop and dic_cop[l] > 0:
                        dic_cop[l] -= 1
                    else:
                        is_match = False
                        break
                if is_match: longest = max(longest, len(word))
        return longest

'''
Other Solution
Time: O(n * m)
Space: O(m + k)
'''

class Solution:
    def solve(self, words, letters):
        lc = Counter(letters)
        maxL = 0
        for w in words:
            wc = Counter(w)
            if wc == (wc & lc):
                maxL = max(maxL, len(w))
        return maxL
