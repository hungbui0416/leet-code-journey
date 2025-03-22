import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n, 0)

        heap = []
        for n in d.keys():
            heapq.heappush(heap, (d[n], n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    
# time:     O(klogn)
# space:    O(n)
