"""
Problem: Binary Tree Zigzag Level Order Traversal — Given the root of a binary tree, return the zigzag level order traversal of its nodes' values (i.e., from left to right, then right to left for the next level and alternate between). Key constraints: Node count is in [0, 2000] and -100 <= Node.val <= 100.
Source: LeetCode #103 (https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
Solution Pattern: Breadth-First Search (Level-Order Traversal with Alternating Direction)
Complexity (My Solution):
    - Time: O(N) — Each node is enqueued and dequeued once; reversing alternating levels takes O(K) where sum of K is N.
    - Space: O(W) — Auxiliary space for queue bounded by the maximum tree width W (O(N) in a balanced tree).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        even = True  # left to right

        if not root:
            return []
        queue = deque()
        queue.append(root)

        level = []
        while queue:
            size = len(queue)

            curr_level = []

            for _ in range(size):
                node = queue.popleft()
                curr_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Append current level directly or reversed depending on alternating depth parity
            level.append(curr_level) if even else level.append(curr_level[::-1])

            even = not even

        return level
