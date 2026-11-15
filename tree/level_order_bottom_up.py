"""
Problem: Binary Tree Level Order Traversal II — Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values (i.e., from left to right, level by level from leaf to root). Key constraints: Node count is in [0, 2000] and -1000 <= Node.val <= 1000.
Source: LeetCode #107 (https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
Solution Pattern: Breadth-First Search (Queue-based Level-by-Level Traversal)
Complexity (My Solution):
    - Time: O(N) — Every node is enqueued, dequeued, and appended once, followed by an O(H) list reversal.
    - Space: O(W) — Queue holds at most the maximum level width W of the tree (up to N/2 nodes).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)

        level = []

        while queue:
            curr_lvl = []
            size = len(queue)

            # Snapshot queue length to process all nodes at current depth before advancing
            for _ in range(size):
                node = queue.popleft()
                curr_lvl.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level.append(curr_lvl)

        level.reverse()
        return level
