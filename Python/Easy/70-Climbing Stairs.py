class Solution:
    def climbStairs(self, n: int) -> int:
        def C(ones,ttw):
            upper,lower = 1, 1
            ones = min(ones,ttw-ones)
            for i in range(ttw,ttw-ones,-1):
                upper *= i
            #print("upper:",upper)
            for i in range(1,ones+1):
                lower *= i
            #print("lower:",lower)
            return int(upper/lower)
            
        def count_distinct(i):
            ones = n-2*i
            total_ways = n - i #ones + i
            return C(ones,total_ways)
        max_twos = n//2
        method_count = 0
        for i in range(max_twos+1): #from no 2-steps to max 2 steps
            print(i,count_distinct(i))
            method_count += count_distinct(i)
            
        return method_count