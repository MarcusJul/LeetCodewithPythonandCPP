class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        strs = sorted(strs)
        com = strs[0]
        while(com!=''):
            found = True
            for i in range(1,len(strs)):
                if com not in strs[i][0:len(com)]:
                    found = False
                    break
            if found == True:
                break
            else:
                com = com[:-1]
        return com