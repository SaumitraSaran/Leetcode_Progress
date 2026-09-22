class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        temp = n
        if temp == 1:
            return True
        if temp % 2 != 0 or temp == 0:
            return False
        while temp % 2 != 1:
            temp = temp//2
            count += 1

        return 2**count == n