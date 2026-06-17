class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 2: return False
        
        dt = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        st = []

        for p in s:
            if p not in dt:
                st.append(p)

            else:
                if not st or st.pop() != dt[p]:
                    return False

        if st: return False

        return True