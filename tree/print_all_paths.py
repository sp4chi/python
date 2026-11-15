"""
Problem: Binary Tree Paths — Given the root of a binary tree, return all root-to-leaf paths in any order. Key constraints: Node count is in [1, 100] and -100 <= Node.val <= 100.
Source: LeetCode #257 (https://leetcode.com/problems/binary-tree-paths/)
Solution Pattern: Backtracking (DFS Pre-order Traversal)
Complexity (My Solution):
    - Time: O(N^2) — Each node is visited once; path string construction takes O(H) for each of the leaves.
    - Space: O(H) — Auxiliary stack space and path list size scale with tree height H.
"""

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
            # Backtrack path list before returning to parent caller
            path.pop()

        if not root.left and not root.right:
            l.append(str(root.val))
            return l

        paths(root, path)

        return l
