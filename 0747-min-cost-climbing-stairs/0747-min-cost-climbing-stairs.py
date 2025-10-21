class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[-1], dp[-2])


# 내가 접근했던 방법(오답 ㅠㅠ)
# class Solution(object):
#     def minCostClimbingStairs(self, cost):
#         """
#         :type cost: List[int]
#         :rtype: int
#         """
#         start=0
#         total=0
#         # if cost[0]>=cost[1]:
#         #     start=1
#         if len(cost)==3 and (cost[0]+cost[2]>=cost[1]):
#             return cost[1]
#         # if len(cost)==4 and (cost[1]+cost[3]<=cost[0]+cost[2]):
#         #     return cost[1]+cost[3]
#         # total+=cost[start]   
#         while start < len(cost)-2:
            
#             total+=cost[start]   
#             print(start,"-",cost[start],"- total: ",total)
#             if cost[start+1]<cost[start+2]:
#                 start+=1
#             else:
#                 start+=2
#                 if start==len(cost)-1:
#                     total+=cost[start]   
#                     print(start,"-",cost[start],"- total: ",total)
            
            
#         return total