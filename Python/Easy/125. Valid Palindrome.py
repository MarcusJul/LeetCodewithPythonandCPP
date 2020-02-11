class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True
        if len(s)==1:
            return True
        ltr = ''
        for char in s:
            if char.isalpha() or char.isnumeric():
                ltr += char.lower()
        if len(ltr)!=0: #",."
            for li in range(len(ltr)):
                if li < len(ltr)-1-li:
                    if ltr[li] == ltr[len(ltr)-1-li]:
                        pass
                    else:
                        return False
                else:
                    return True
        else:
            return True
        
            