class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            remains=target-nums[i]

            if remains in dic:
                return [dic[remains],i]
            
            dic[nums[i]]=i

        
