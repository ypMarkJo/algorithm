class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
 
        ans=0
        while len(grid[0])!=0:
            maximum=0
            for arr in grid:
                print(arr)
                if maximum<max(arr):
                    maximum=max(arr)
                del_idx=0
                for i in range(len(arr)):
                    if arr[del_idx] <= arr[i]:
                        del_idx=i
                del arr[del_idx]
            print(maximum)
            ans+=maximum
            
        return ans
        