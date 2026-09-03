class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dex = 0
        if target in nums:
            dex = nums.index(target)
        else:
            l = nums
            l.append(target)
            l.sort()
            dex = nums.index(target)
        
        return dex