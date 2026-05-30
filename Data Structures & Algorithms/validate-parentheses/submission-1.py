class Solution:
    def isValid(self, s: str) -> bool:
        
        ref = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        st = []

        for c in s:
            if c not in ref:
                st.append(c)
            else:
                if not st:
                    return False
                
                if st.pop() != ref[c]:
                    return False

        if len(st) > 0:
            return False

        return True