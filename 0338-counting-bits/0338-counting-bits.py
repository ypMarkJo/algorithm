class Solution(object):
    # def countBits(self, n):
    #     """
    #     count 방식
    #     :type n: int
    #     :rtype: List[int]
    #     """
    #     output=[]
    #     for i in range(n+1):
    #         output.append(bin(i)[2:].count('1'))
    #     return output

     def countBits(self, n):
        """
        dp 방식
        :type n: int
        :rtype: List[int]
        """
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=dp[i>>1]+(i&1)
        return dp
