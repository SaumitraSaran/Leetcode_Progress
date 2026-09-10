class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums_set = set(nums)
        return [i for i in range(1, n + 1) if i not in nums_set]
