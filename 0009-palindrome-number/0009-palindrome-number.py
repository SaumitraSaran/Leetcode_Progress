class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        flag = True

        if x < 0:
            flag = False
        else:
            temp = x
            reverse = 0

            while temp > 0:
                digit = temp % 10
                reverse = reverse * 10 + digit
                temp = temp // 10

            flag = (reverse == x)
        
        return flag