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
    # def rangeSumBST(self, root, low, high):
    #     if not root:
    #         return 0
    #     if root.val < low:
    #         # 현재 노드 값이 low 보다 작으면 -> 오른쪽만 탐색(왼쪽 무시)
    #         return self.rangeSumBST(root.right, low, high)
    #     if root.val > high:
    #         # 현재 노드 값이 high 보다 크면 -> 왼쪽만 탐색(오른쪽 무시)
    #         return self.rangeSumBST(root.left, low, high)

    # # 현재 노드 값이 범위 안에 있다면 -> 왼쪽 + 현재 + 오른쪽 탐색
    #     return (
    #         # 중위순회 고고링
    #         root.val +
    #         self.rangeSumBST(root.left, low, high) +
    #         self.rangeSumBST(root.right, low, high)
    #     )