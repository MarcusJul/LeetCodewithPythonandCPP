class Solution:
    def romanToInt(self, s: str) -> int:
        d1 = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        d2 = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        lst = [0]*len(s) 
        def findse(si,s):
            ei = si+len(s)-1
            return (si,ei)
        # Loop for 2 digits
        i,count=0,0
        while(i<len(s)):
            if s[i:i+2] in d1:
                count+=d1[s[i:i+2]] 
                lst[i], lst[i+1] = 1,1
                i+=2
            else:
                i+=1
        
        # Loop for 1 digits
        i=0
        while(i<len(s)):
            if lst[i]!=1:
                if s[i] in d2:
                    count+=d2[s[i]]
            i+=1
                    
                    
        return count
        