class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert to set to remove duplicates; create a counter
        count = 0
        nums = set(nums)
        
        # loop through nums; set length; while next number exists - increase length; 
        for num in nums:
            length = 1
            while num + length in nums:
                length += 1
            # store the max of length and count
            count = max(count, length)
            
        # return count
        return count