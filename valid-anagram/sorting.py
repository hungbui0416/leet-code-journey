class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
    
# time:     O(nlogn + mlogm)
# space:    O(1) or O(n + m) depending on sorting algo

        