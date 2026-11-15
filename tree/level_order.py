"""
Problem: Binary Tree Level Order Traversal — Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level). Key constraints: Node count is in [0, 2000] and -1000 <= Node.val <= 1000.
Source: LeetCode #102 (https://leetcode.com/problems/binary-tree-level-order-traversal/)
Solution Pattern: Breadth-First Search (Queue-based Level-by-Level Traversal)
Complexity (My Solution):
    - Time: O(N) — Every node is processed and added to its respective level list once.
    - Space: O(W) — Queue auxiliary space is bounded by the maximum tree width W (O(N) for balanced trees).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        level = []
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            current_level = []

            # Process all nodes at current level using batch queue snapshot
            for _ in range(size):
                node = queue.popleft()
                current_level.append(node.val)

                left = node.left
                right = node.right

                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            level.append(current_level)

        return level
