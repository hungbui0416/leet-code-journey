class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        A = []
        for i, n in enumerate(nums):
            A.append((n, i))
        
        A.sort()
        i, j = 0, len(nums)-1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return A[i][1], A[j][1]
            elif cur < target:
                i += 1
            else:
                j -= 1
        
        return ()

# time:     O(nlogn)
# space:    O(n)