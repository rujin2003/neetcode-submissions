# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSametree(self,p,q):
        if p == None and q == None:
            return True 
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        left = self.isSametree(p.left, q.left)
        right = self.isSametree(p.right , q.right)
        return (left and right)
      
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        if root is None:
            return False
        if self.isSametree(root,subRoot):
            return True
        return (
            self.isSubtree(root.left,subRoot)
            or self.isSubtree(root.right , subRoot)
        )
        