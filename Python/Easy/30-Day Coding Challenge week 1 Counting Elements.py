class Solution:
    def countElements(self, arr: List[int]) -> int:
        lst = sorted(arr)
        d = {}
        count = 0
        def findtar(tar, starti, lst, l):
            i = starti+1
            while(i<l):
                if lst[i]>=tar:
                    return i
                else:
                    i+=1
            return i
        l = len(lst)
        i = 0
        while(i<l):
            ret = findtar(lst[i]+1, i, lst, l)
            if ret<l:
                if lst[ret]==lst[i]+1:
                    count += ret-i
                i = ret
            else:
                return count
        return count