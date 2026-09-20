# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        main = []
        temp = []

        def helper(node, remaining):
            # empty subtree
            if not node:
                return

            remaining -= node.val
            temp.append(node.val)

            # leaf node
            if not node.left and not node.right:
                if remaining == 0:
                    main.append(temp[:])
            # not a leaf
            else:
                helper(node.left, remaining)
                helper(node.right, remaining)
            temp.pop()

        helper(root, targetSum)
        return main
