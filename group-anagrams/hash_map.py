from collections import defaultdict

class Solution(object):  
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for s in strs:
            f = [0] * 26
            for c in s:
                f[ord(c)-ord('a')] += 1
            d[tuple(f)].append(s)
        
        return list(d.values())
    
# time:     O(n*m)
# space:    O(n*m)