class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        mp = defaultdict(int)

        for i in range(len(nums)):
            if not mp[nums[i]]:
                mp[nums[i]] = 1 + mp[nums[i]+1] + mp[nums[i]-1]
                mp[nums[i] - mp[nums[i]-1]] = mp[nums[i]]
                mp[nums[i] + mp[nums[i]+1]] = mp[nums[i]]
                res = max(res,mp[nums[i]])

        return res