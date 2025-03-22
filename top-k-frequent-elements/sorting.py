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
        
        arr = []
        for n, f in d.items():
            arr.append([f, n])
        arr.sort(reverse=True)

        res = []
        for i in range(k):
            res.append(arr[i][1])

        # arr = []
        # for n, f in d.items():
        #     arr.append([f, n])
        # arr.sort()

        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        
        return res

# time:     O(nlogn)
# space:    O(n)
