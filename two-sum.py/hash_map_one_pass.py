class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return i, prev[diff]
            prev[n] = i
        
        return ()

# time:     O(n)
# space:    O(n)