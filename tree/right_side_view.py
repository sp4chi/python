"""
Problem: Binary Tree Right Side View — Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom. Key constraints: Node count is in [0, 100] and -100 <= Node.val <= 100.
Source: LeetCode #199 (https://leetcode.com/problems/binary-tree-right-side-view/)
Solution Pattern: Breadth-First Search (Level-Order Traversal with Queue)
Complexity (My Solution):
    - Time: O(N) — Every node is visited and processed once in the BFS level traversal.
    - Space: O(W) — Queue holds at most the maximum level width W of the tree (O(N) for balanced trees).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        lvl = []
        while queue:
            size = len(queue)
            curr_lvl = []
            for i in range(size):
                node = queue.popleft()
                curr_lvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # The rightmost node visible at each level is the last element processed in level order
            lvl.append(curr_lvl[-1])
        return lvl
