class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        res = [0] * 26

        for r in ransomNote:
            res[ord(r) - ord('a')] += 1

        for m in magazine:
            res[ord(m) - ord('a')] -= 1
            
        for r in res:
            if r > 0:
                return False

        return True