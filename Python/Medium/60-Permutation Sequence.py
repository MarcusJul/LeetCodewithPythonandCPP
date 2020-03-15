class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n==1:
            return '1'
        def per(num, alst, tlst, flag, count):
            if num==2:
                return [tlst+[alst[0],alst[1]], tlst+[alst[1],alst[0]]], True if count>=k else False, count+2
            else:  
                ret_lst = []
                for i in range(len(alst)):
                    lst, flag, count = per(num-1, alst[:i]+alst[i+1:], tlst+[alst[i]], flag, count)               
                    ret_lst += lst
                    if flag==True:
                        break
                return ret_lst, flag, count
        
        alst = [i for i in range(1,n+1)]
        
        plst, flag, count = per(n, alst, [], False, 0)
        return ''.join(list(map(str, plst[k-1])))