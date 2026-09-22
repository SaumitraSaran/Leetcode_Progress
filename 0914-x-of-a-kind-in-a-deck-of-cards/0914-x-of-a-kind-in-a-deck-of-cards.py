class Solution(object):
    
    
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        dic = dict.fromkeys(list(set(deck)), 0)
        for i in range(len(deck)):
            if deck[i] in dic:
                dic[deck[i]] += 1
        values = list(dic.values())
        g = values[0]
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        for i in range(1, len(values)):
            g = gcd(g, values[i])
        return g >= 2
        