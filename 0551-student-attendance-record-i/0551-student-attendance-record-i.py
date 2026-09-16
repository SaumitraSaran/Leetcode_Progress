class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        substring = "LLL"

        if s.count("A") < 2 and substring not in s:
            return True

        return False