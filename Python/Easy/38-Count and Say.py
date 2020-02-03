class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        else:
            cur = "1"
            for i in range(1,n):
                # read current str
                j=0
                cur_num = cur[j]
                count = 0
                length = len(cur)
                lst_comp = []
                while(j<length):
                    if cur[j]==cur_num:
                        count+=1
                    else:
                        lst_comp.append({cur_num:count})
                        cur_num = cur[j]
                        count=1
                    j+=1
                lst_comp.append({cur_num:count})
                #print(lst_comp)
                # generate next str
                cur = ""
                for d in range(len(lst_comp)):
                    dic = lst_comp[d]
                    for k,v in dic.items():
                        cur+=str(v)
                        cur+=str(k)
                #print(cur)
        return cur