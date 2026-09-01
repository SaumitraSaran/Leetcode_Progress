class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = ""
        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[0][j] != strs[i][j]:
                    return common;

            common += strs[0][j]

        return common;
        