# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None

        def helper_post(root):

            nonlocal prev

            # no subtree
            if not root:
                return None

            helper_post(root.right)
            helper_post(root.left)

            root.right = prev
            root.left = None
            prev = root
            # if root.left:
            #     root.right = root.left
            #     root.left = None
            #     b.right = a

        helper_post(root)

        def helper_pre(root):

            # no subtree
            if not root:
                return None

            right = root.right

            a = helper_post(root.left)  # 4
            b = helper_post(root.right)  # 6

            if root.left:
                root.right = root.left
                root.left = None
                a.right = right
            return b or a or root

        helper_pre(root)
