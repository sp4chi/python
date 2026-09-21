# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#                      1
#                    /   \
#                   2     2
#                  / \   / \
#                 3   n n   3
#                /           \
#               4             4
#              / \
#             n   n
class Solution:
    def height(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        left = self.height(root.left)
        if left == -1:
            return -1

        right = self.height(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        return self.height(root) != -1
