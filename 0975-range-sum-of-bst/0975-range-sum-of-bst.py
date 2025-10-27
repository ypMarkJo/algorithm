# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        self.total=0
        self.low=low
        self.high=high
        self.inorder(root)
        return self.total
        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            if root.val >=self.low and root.val <=self.high:
                self.total+=root.val
            self.inorder(root.right)
