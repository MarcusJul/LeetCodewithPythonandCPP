class Solution:
    def reverse(self, x: int) -> int:
        store = []
        if x>0:
            temp = x
            while(True):
                store.append(str(temp%10))
                if temp//10>0:
                    temp = temp//10
                else:
                    break
            ret = int(''.join(store))
        elif x<0:
            temp = -x
            while(True):
                store.append(str(temp%10))
                if temp//10>0:
                    temp = temp//10
                else:
                    break
            ret = -int(''.join(store))
        # x==0
        else:
            ret = 0
        if ret>2**31 or ret<-(2**31):
            return 0 
        else:
            return rets