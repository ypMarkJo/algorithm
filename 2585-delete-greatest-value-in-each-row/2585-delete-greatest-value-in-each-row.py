class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
 
        ans=0
        while len(grid[0])!=0:
            max=0
            for arr in grid:
                del_idx=0
                for i in range(len(arr)):
                    if arr[del_idx] <= arr[i]:
                        del_idx=i
                        if arr[i] > max:
                            max=arr[i]
                del arr[del_idx]
            ans+=max
            
        return ans
        