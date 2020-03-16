class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def geneList(lst):
            if lst==[]:
                return [1]
            ret = [lst[0]]
            for i in range(len(lst)-1):
                ret.append(lst[i]+lst[i+1])
            
            ret.append(lst[-1])
            return ret
        
        ret_lst = []
        lst = []
        for i in range(numRows):
            lst = geneList(lst)
            ret_lst.append(lst)
        
        return ret_lst