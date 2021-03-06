# https://leetcode.com/problems/power-of-two/submissions/
# 2021 12.21
# 2022年07月13日 12:24:41

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # # v1 common 32ms slow
        # for i in range(n):
        #     if 2**i==n:
        #         return True
        #     elif 2**i>n:
        #         return False
        
        # v2 copied brilliant oneliner 24ms bitwise and to detect if n is the form like 100000b
        # all power of two denoted in binary is like 1000b : 8=1000b 4=100b 2=10b
        # n-1 = 0111b like 7=0111b 3=011b 1=01b
        # like n=8  then n&(n-1)=1000b&0111b=0 
        # so if n is power of two, n&(n-1)==0 
        return (n>0) and (n & (n-1))==0

        # # v3 copied like v2 bitwise oneliner 24ms
        # return n > 0 and bin(n).count('1') == 1



        # # 2022年07月13日 12:13:21
        # # v1
        # return n>=0 and str(bin(n)).count('1')==1
        
        # # 2022年07月13日 12:14:41
        # # v2
        # if n<=0: return False
        # while n & 1 ==0 :
        #     n=n>>1
        # return n==1

        # v2.1 2022年07月14日 09:39:53
        while n>0 and n&1==0:
            n>>=1
        return n==1
    
        # # 2022年07月13日 12:19:38
        # # v3
        # i=1
        # while i<n:
        #     i=i<<1
        # return i==n