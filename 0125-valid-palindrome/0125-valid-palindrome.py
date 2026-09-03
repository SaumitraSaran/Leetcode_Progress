class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = True
        s = ''.join(c.lower() for c in s if c.isalnum())
        i = 0
        while(flag and i<len(s)):
            if s[i] != s[len(s) - 1 - i]:
                flag = False
            i+=1

        return flag
