class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        operations=0
        bit='0'
        for cur in target:
            if cur != bit:
                operations+=1
                bit =cur              
        return operations