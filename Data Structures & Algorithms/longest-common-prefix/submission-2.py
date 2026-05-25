class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        str = ""
        for k in range(len(strs[0])):
            for i in range(len(strs)):
                try:
                    if strs[i][k] == strs[0][k]:
                        count = count + 1
                    else:
                        break
                except IndexError:
                        break
            
            if count == len(strs):
                str = str + strs[0][k]
                count = 0
            else:
                break
        return str
            
