# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        l = []
        path = []

        def paths(root, path):
            # if no subtree
            if not root:
                return None

            path.append(str(root.val))

            # if leaf, save it
            if not root.left and not root.right:
                s = "->".join(path)
                l.append(s)
            else:
                paths(root.left, path)
                paths(root.right, path)

            # cleanup / backtrack
            path.pop()

        if not root.left and not root.right:
            l.append(str(root.val))
            return l

        paths(root, path)

        return l
