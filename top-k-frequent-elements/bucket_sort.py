class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cs = {}
        fs = [[] for i in range(len(nums)+1)]

        for n in nums:
            cs[n] = 1 + cs.get(n, 0)
        
        for n, f in cs.items():
            fs[f].append(n)

        res = []
        for i in range(len(fs) - 1, 0, -1):
            for n in fs[i]:
                res.append(n)
                if len(res) == k:
                    return res
    
# time:     O(n)
# space:    O(n)
