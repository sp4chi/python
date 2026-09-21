# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def helper(root, min_bound, max_bound):
            if not root:
                return True

            if not (min_bound < root.val < max_bound):
                return False

            a = helper(root.left, min_bound, root.val)
            b = helper(root.right, root.val, max_bound)
            return a and b

        return helper(root, float("-inf"), float("inf"))
