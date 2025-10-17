class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ret=0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    ret+=1
        return ret