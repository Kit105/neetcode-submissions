class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashStrS = {}
        hashStrT = {}

        for a in s:
            if a in hashStrS:
                hashStrS[a] += 1
            else:
                hashStrS[a] = 1
        
        for b in t:
            if b in hashStrT:
                hashStrT[b] += 1
            else:
                hashStrT[b] = 1
                

        return hashStrS == hashStrT    