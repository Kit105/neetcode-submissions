class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        hm = set()
        res = []
        nums.sort()

        for i,n in enumerate(nums):

            if n < 1 and n not in hm:

                l = i + 1
                r = len(nums) - 1

                while l < r:

                    sum = nums[l] + nums[r]

                    if sum + n < 0:
                        l += 1
                    elif sum +n > 0:
                        r -= 1
                    else:
                        if [n,nums[l], nums[r]] not in res:
                            res.append([n,nums[l], nums[r]])
                        l += 1
                
            hm.add(n)
        
        return res