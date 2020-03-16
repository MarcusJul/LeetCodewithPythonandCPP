class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def geneList(lst):
            if lst==[]:
                return [1]
            ret = [lst[0]]
            for i in range(len(lst)-1):
                ret.append(lst[i]+lst[i+1])
            
            ret.append(lst[-1])
            return ret
        
        ret_lst = []
        lst = [1]
        for i in range(rowIndex):
            lst = geneList(lst)
        
        return lst