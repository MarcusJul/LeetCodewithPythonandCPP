class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret_lst = []
        d = {
            '2':'abc',
            '3':'def',
            '4':'ghi', 
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        if digits=='':
            return None
        def enum(num,ps):
            alphabets = d[num[0]]
            lst = [ps+al for al in alphabets]
            if len(num)==1:
                return lst
            else:
                ret_lst = []
                for psal in lst:
                    l = enum(num[1:],psal)
                    ret_lst+=l
                return ret_lst
        return enum(digits,'')