# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, l):
        if root == None:
            return

        self.helper(root.left, l)
        l.append(root.val)
        self.helper(root.right, l)

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        l = []
        self.helper(root, l)
        return l
