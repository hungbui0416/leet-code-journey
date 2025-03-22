from collections import defaultdict

class Solution(object):  
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for s in strs:
            sorted_str = str(sorted(s))
            d[sorted_str].append(s)
        
        return list(d.values())
    
# time:     O(n*m*logm)
# space:    O(n*m)