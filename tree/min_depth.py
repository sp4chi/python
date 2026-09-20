# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#               2
#             /   \
#          null.   3
#                /   \
#              null.  4
#                    /  \
#                  null  5
#                       /  \
#                     null  6
# A leaf node is the node whose childrens are null
class Solution:
    def helper(self, root):
        if not root:
            return 0

        a = self.helper(root.left)
        b = self.helper(root.right)
        ans = 1

        if a == 0 and b == 0:
            ans = 1
        elif a == 0 and b != 0:
            ans = b + 1
        elif a != 0 and b == 0:
            ans = a + 1
        else:
            ans = min(a, b) + 1

        return ans

    def minDepth(self, root: TreeNode | None) -> int:
        return self.helper(root)
