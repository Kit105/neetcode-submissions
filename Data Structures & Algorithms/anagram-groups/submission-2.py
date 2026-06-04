from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)

        for s in strs:
            s_sorted = ''.join(sorted(s, reverse=True))

            hashmap[s_sorted].append(s)


        return list(hashmap.values())