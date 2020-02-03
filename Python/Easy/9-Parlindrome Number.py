class Solution:
    def isPalindrome(self, x: int) -> bool:
        def reverse(x):
            return
        if x>=0:
            if x<10:
                return True
            else:
                store = []
                temp = x
                while(True):
                    store.append(str(temp%10))
                    if temp<10:
                        break 
                    else:
                        temp = temp//10
                x_r = int(''.join(store))
                if x_r == x:
                    return True
                else:
                    return False
        elif x==0:
            return True
        else:
            return False