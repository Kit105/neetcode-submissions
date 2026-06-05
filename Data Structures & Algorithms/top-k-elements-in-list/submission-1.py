class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        hashmap = [[] for x in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num,0)
            
        for num, c in count.items():
            hashmap[c].append(num)

        res = []
        for i in range(len(hashmap) -1, 0 , -1):
            for n in hashmap[i]:
                res.append(n)
                if len(res) == k:
                    return res