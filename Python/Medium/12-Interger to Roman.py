class Solution:
    def intToRoman(self, num: int) -> str:
        seq = ''
        if num//1000>0:
            i = num//1000
            seq+='M'*i

        num = num%1000  
        i1 = num//100
        i2 = num//500
        if i2>0:# left>500
            if i1==9:
                seq+='CM'
            else:
                seq+='D'+'C'*(i1-5)
        else:
            if i1==4:
                seq+='CD'
            else:
                seq+='C'*i1

        num = num%100
        i1 = num//10
        i2 = num//50
        if i2>0: #left>50:
            if i1==9:
                seq+='XC'
            else:
                seq+='L'+'X'*(i1-5)
        else:
            if i1==4:
                seq+='XL'
            else:
                seq+='X'*i1

        num = num%10
        i1 = num
        i2 = num//5
        if i1>5:
            if i1==9:
                seq+='IX'
            
            else:
                seq+='V'+'I'*(i1-5)
        else:
            if i1==4:
                seq+='IV'
            elif i1==5:
                seq+='V'
            else:
                seq+='I'*i1
        return seq
                
                
                
