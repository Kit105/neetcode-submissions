class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""
        seperator = "#"
        for s in strs:
            enc_str += str(len(s)) + seperator + s
        return enc_str

    def decode(self, s: str) -> List[str]:
        i,j = 0, 0
        res = []
        while i <= len(s) - 1:
            # j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i=j
        return res
    
    