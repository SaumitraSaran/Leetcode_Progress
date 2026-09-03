class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = -1
        length = len(digits)
        if digits[i] < 9 :
                digits[i] += 1
        else:
            while(digits[i] == 9):
                digits[i] = 0
                i -= 1
                if abs(i) > len(digits):
                    return [1] + digits

            digits[i] += 1

        return digits
            
            