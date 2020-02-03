class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        sig = -1
        if needle in haystack:
            n = len(needle)
            for i in range(len(haystack)-n+1):
                if haystack[i:i+n]==needle:
                    return i
        else:
            return sig