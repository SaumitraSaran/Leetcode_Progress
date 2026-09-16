class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ind = 0
        if len(word) == 1:
                return True

        if len(word) == 2 and word[0].islower() and word[1].isupper():
                return False

        if word[ind].isupper() and word[ind+1].isupper():
            for i in range(ind+2, len(word)):
                if word[i].islower():
                    return False

        if word[ind].isupper() and word[ind+1].islower():
            for j in range(ind+2, len(word)):
                if word[j].isupper():
                    return False

        if word[ind].islower():
            for k in range(ind+1, len(word)):
                if word[k].isupper():
                    return False

        return True