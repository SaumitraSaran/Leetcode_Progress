class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = nums1 + nums2
        l.sort()
        mid = len(l)//2
        if len(l) % 2 == 0:
            return (l[mid - 1] + l[mid]) / 2.0
        else:
            return l[mid]