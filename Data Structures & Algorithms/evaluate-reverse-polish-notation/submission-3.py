class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        res = []

        for token in tokens:
            if token not in "+-*/":
                res.append(int(token))
            else:
                b = int(res.pop())
                a = int(res.pop())
                if token == "+":
                    res.append(a+b)
                elif token == "-":
                    res.append(a-b)
                elif token == "*":
                    res.append(a*b)
                else:
                    res.append(int(a/b))

        return res.pop()