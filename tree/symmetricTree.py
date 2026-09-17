# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, leftTree: TreeNode, rightTree: TreeNode):
        if not leftTree and not rightTree:
            return True

        if not leftTree or not rightTree:
            return False

        if leftTree.val != rightTree.val:
            return False

        a = self.helper(leftTree.left, rightTree.right)
        b = self.helper(rightTree.left, leftTree.right)
        return a and b

    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root == None:
            return True

        return self.helper(root.left, root.right)
