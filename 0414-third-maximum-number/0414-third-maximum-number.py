class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        thirdMax = 0
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            thirdMax = max(nums)
        else:
            nums.pop()
            nums.pop()
            thirdMax = nums.pop()
        return thirdMax