class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i = len(s) - 1
        while i >= 0:
            if s[i] != " " and i >=0:
                res = 0
                while s[i] != " " and i >= 0:
                    res += 1
                    i -= 1
                return res
            i -= 1