from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l , r = 1, max(piles)
        res = r
        while l <= r:
            rate = (r + l) // 2
            hour = 0

            for pile in piles:
                hour += ceil(float(pile)/rate)
            
            if hour > h:
                l = rate + 1
            else:
                res = rate
                r = rate - 1

        return res
