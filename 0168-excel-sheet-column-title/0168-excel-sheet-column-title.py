class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            ans = S[columnNumber % 26] + ans
            columnNumber //= 26

        return ans