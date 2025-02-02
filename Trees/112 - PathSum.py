# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def same(root, curr):
            if not root:
                return False

            curr += root.val

            if not root.left  and not root.right:
                return curr == targetSum

            return same(root.left, curr) or same(root.right, curr)
        
        return same(root, 0)
            
            
