class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output=[]
        for i in range(n+1):
            output.append(bin(i)[2:].count('1'))
        return output

