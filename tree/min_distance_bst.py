"""
Problem: Minimum Absolute Difference in BST — Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree. Key constraints: Node count is in [2, 10^4] and 0 <= Node.val <= 10^5 (identical to LeetCode #783 Minimum Distance Between BST Nodes).
Source: LeetCode #530 (https://leetcode.com/problems/minimum-absolute-difference-in-bst/)
Solution Pattern: In-order Traversal (DFS)
Complexity (My Solution):
    - Time: O(N) — Visits each node exactly once in an in-order sequence.
    - Space: O(H) — Auxiliary call stack space proportional to tree height H; O(log N) for balanced trees and O(N) in the worst case for skewed trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        md = float("inf")

        def dfs(node):
            nonlocal prev, md  # no recreation,
            if not node:
                return float("inf")

            dfs(node.left)

            # In-order traversal visits BST keys in sorted order; track min adjacent gap
            if prev is not None:
                md = min(md, node.val - prev)
            prev = node.val

            dfs(node.right)

        dfs(root)

        return md

        # def dfs(node,high,low):
        #     if not node:
        #         return high - low

        #     a = dfs(node.left, node.val, low)
        #     b = dfs(node.right, high, node.val)

        #     return min(a,b)

        # return dfs(root, float('inf'), float('-inf'))

        # if not root:
        #     return None

        # minn = float('inf')
        # queue = deque()
        # queue.append((root, float('inf'), float('-inf'))) # node, high, low

        # while queue:

        #     node, high, low = queue.popleft()

        #     minn = min(minn, high - node.val, node.val - low )

        #     if node.left:
        #         queue.append((node.left, node.val, low))
        #     if node.right:
        #         queue.append((node.right, high, node.val))

        # return minn
