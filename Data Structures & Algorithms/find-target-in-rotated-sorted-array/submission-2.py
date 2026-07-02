class Solution:



    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0, len(nums) - 1

        while l < r:

            m =(r + l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        start = l

        def binary_search(lo:int, hi:int) -> int:
            while lo <= hi:
                mid = (lo+hi)//2
                if target == nums[mid]: return mid
                elif target < nums[mid]: hi = mid - 1
                else: lo = mid + 1
            return -1

        res = binary_search(0, start - 1)
        if res != -1:
            return res


        return binary_search(start, len(nums) - 1)        