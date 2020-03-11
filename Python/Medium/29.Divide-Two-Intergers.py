class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0:
            return 0
        if dividend*divisor>=0:
            if dividend>0:
                di, dv = dividend, divisor
            else:
                di, dv = -dividend, -divisor
            flag = True
        else:
            if dividend>0 and divisor<0:
                di, dv = dividend, -divisor
            else:
                di, dv = -dividend, divisor
            flag = False
        if di<dv:
            return 0
        if dv==1:
            ret = di if flag else -di
            if ret>=2147483648:
                return 2147483647
            else:
                return ret
                
        def checkvalid(base, num, tar):
            if base*num<=tar and base*(num+1)>tar:
                return True
            else:
                return False
            
        left, right = 1, di
        mid = int((left+right)/2)
        while(True):
            if checkvalid(dv,mid,di):
                ret = mid if flag else -mid
                if ret >= 2147483648:
                    return 2147483647
                else:
                    return ret
            else:
                if dv*mid>di:
                    right = mid
                else:
                    left = mid
                mid = int((left+right)/2)
                