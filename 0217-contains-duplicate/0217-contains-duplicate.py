class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        isDistinct = (len(nums) == len(set(nums)))
        return not isDistinct