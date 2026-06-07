class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        res2 = [1] * len(nums)
        ans = []
        pref = 1
        suff = 1


        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]

        for i in range(len(nums) -1, -1, -1):
            res2[i] = suff
            suff *= nums[i]

        for a,b in zip(res,res2):
            ans.append(a*b)

        return ans