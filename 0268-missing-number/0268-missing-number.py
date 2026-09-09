class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = list(range(0, len(nums)+1))
        for i in nums:
            if i in l:
                l.remove(i)
        
        return l.pop()