class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}
        for n in nums:
            if n in seen:
                return True
            seen[n] = 0
        return False
    
# time:     O(n)
# space:    O(n)