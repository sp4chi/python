# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        path_p = []
        path_q = []

        def helper(root, k, path):
            if not root:
                return False

            if root.val == k:
                path.append(root)
                return True

            a = helper(root.left, k, path)
            b = helper(root.right, k, path)

            if a or b:
                path.append(root)
                return True

            return False

        helper(root, p.val, path_p)
        helper(root, q.val, path_q)

        i = 0
        path_p.reverse()
        path_q.reverse()

        ans = 0
        while i < min(len(path_p), len(path_q)):
            if path_p[i].val == path_q[i].val:
                ans = i
            else:
                break
            i += 1

        return path_p[ans]
