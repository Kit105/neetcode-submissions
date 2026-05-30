class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary
        output = {}
        
        # loop through strs
        # each str get sorted and pushed into the dict
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in output:
                output[sorted_str] += [str]
            else:
                output[sorted_str] = [str]
        
        return list(output.values())
        