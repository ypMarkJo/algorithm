class Solution(object):
    # def countPairs(self, nums, target):
    #     """
    #     내 풀이 : 불필요한 반복구간 수행이 있음.
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     count=0
    #     n=len(nums)
    #     for i in range(n):
    #         for j in range(i+1,n):
    #                 if target>nums[j]+nums[i]:
    #                     count+=1
    #     return count

    def countPairs(self, nums, target):
        """
        정석 풀이: 필요한 구간만 돔.
        """
        nums.sort()
        print(nums)
        ans=0
        i,j=0,len(nums)-1
        
        while i<j:
            if nums[i] + nums[j] < target:
                ans += j - i
                i += 1
            else:
                j -= 1
        return ans