class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
      
        preArr=nums[:n]
        postArr=nums[n:]
        retArr=[]
        for i in range(n):
            retArr.append(preArr[i])
            retArr.append(postArr[i])
        return retArr
