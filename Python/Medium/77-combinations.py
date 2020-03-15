class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # There are two ways to do this
        # One is picking with recursion, one is deleting with recursion
        def per(alst, 
                kcount, 
                tlst # a list of numbers that have been seleted
               ):
            ret_lst = []
            if kcount==1:
                for i in range(len(alst)):
                    ret_lst.append(tlst+[alst[i]])
                return ret_lst
            else:
                for i in range(len(alst)-kcount+1):
                    ret_lst += per(alst[i+1:],kcount-1,tlst+[alst[i]])
                
                return ret_lst
        
        alst = [i for i in range(1,n+1)]
        return per(alst, k, [])