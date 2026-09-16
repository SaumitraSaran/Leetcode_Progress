class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split(" ")
        for i in range(len(l)):
            l[i] = l[i][::-1]
        
        return " ".join(l)