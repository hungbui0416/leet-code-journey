class Solution(object):  
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        for str in strs:
            added = False
            for i in range(len(ans)):
                if self.checkAnagrams(str, ans[i][0]):
                    ans[i].append(str)
                    added = True
                    break

            if not added:
                ans.append([str])
        
        return ans


    def checkAnagrams(self, str1, str2):
        if len(str1) != len(str2):
            return False
        
        vocab1, vocab2 = {}, {}

        for i in range(len(str1)):
            vocab1[str1[i]] = 1 + vocab1.get(str1[i], 0)
            vocab2[str2[i]] = 1 + vocab2.get(str2[i], 0)
        
        return vocab1 == vocab2
        
# time:     O(n^2*m)
# space:    O(n*m)