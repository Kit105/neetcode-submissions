class Solution:

    def alphaNum(self, a:str):

        return (ord('a') <= ord(a) <= ord('z')) or (ord('A') <= ord(a) <= ord('Z')) or (ord('0') <= ord(a) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        
        while l < r:

            while l < r and not self.alphaNum(s[l]):
                l += 1

            while l < r and not self.alphaNum(s[r]):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True