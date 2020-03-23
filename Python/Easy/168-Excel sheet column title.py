class Solution:
    def convertToTitle(self, n: int) -> str:
        d = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',
            11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',
            21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
        
        if n<=26:
            return d[n]
        
        i=1
        while(True):
            if 26**(i)<n and 26**(i+1)>=n:
                break
            else:
                i+=1
        print("i:",i)
        
        ret = ''
        while(True):
            left, right = n//26, n%26
            if right==0: #n is 26*x
                ret = d[26] + ret
                if left!=1:
                    n = left-1
                else: #n==26
                    ret = d[1] + ret
                    break
            else:
                ret = d[right] + ret
                n = left
            if n<=26:
                break
        
        ret = d[max(1,n)] + ret
        
        return ret
                    