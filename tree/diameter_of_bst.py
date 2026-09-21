# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    d = -1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = -1

        def helper(root):
            nonlocal d
            if not root:
                return 0

            a = helper(root.left)
            b = helper(root.right)

            h = max(a, b) + 1

            d = max(d, a + b)

            return h

        helper(root)
        return d
