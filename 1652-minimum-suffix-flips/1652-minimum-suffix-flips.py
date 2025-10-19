class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        operations=0
        n=len(target)
        bit='0'
        for cur in target:
            if cur != bit:
                operations+=1
                bit =cur              
        return operations