class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits)==1:
            num = digits[0]+1
            if num!=10:
                return [num]
            else:
                return [1,0]
        else:
            num = 0
            out = []
            for i in digits:
                num *= 10
                num += i
            num += 1
            num = int(num)
            print(num)
            
            while(num>=1):
                out = [int(num%10)] + out
                num = num//10
            return out