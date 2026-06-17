class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        ht = defaultdict(int)

        for ch in s:
            ht[ch] += 1
            
        for i,c in enumerate(s):
            if ht[c] == 1:
                return i
        return -1