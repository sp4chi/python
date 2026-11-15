"""
Problem: Lowest Common Ancestor of a Binary Tree — Given a binary tree, find the lowest common ancestor (LCA) of two given nodes p and q. Key constraints: Node count is in [2, 10^5], node values are unique, and p and q exist in the tree with p != q.
Source: LeetCode #236 (https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
Solution Pattern: Path-Finding with Backtracking / DFS (Root-to-Node Path Comparison)
Complexity (My Solution):
    - Time: O(N) — Traverses the tree to find root-to-node paths for p and q, then scans the paths.
    - Space: O(H) — Auxiliary call stack space and path storage proportional to tree height H.
"""

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
        # Identify lowest common ancestor as the last matching node along reversed root-to-target paths
        while i < min(len(path_p), len(path_q)):
            if path_p[i].val == path_q[i].val:
                ans = i
            else:
                break
            i += 1

        return path_p[ans]
