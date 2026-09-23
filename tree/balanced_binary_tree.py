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
    # Approach 1
    def isBalanced(self, A):

        def isHeightBalanced(A):

            # return height and balance status, 1 if "balanced", 0 not "balanced",
            # return (height, balance)
            if not A:
                return 0, True

            left_height, left_balance = isHeightBalanced(A.left)
            if not left_balance:
                return left_balance, False

            right_height, right_balance = isHeightBalanced(A.right)
            if not right_balance:
                return right_balance, False

            current_height = max(left_height, right_height) + 1
            current_balance = abs(left_height - right_height) <= 1

            return current_height, current_balance

        height, balance = isHeightBalanced(A)
        return 1 if balance else 0

    # Driver Code for Approach 2
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

    # Approach 2
    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        return self.height(root) != -1
