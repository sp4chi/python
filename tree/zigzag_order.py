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

            level.append(curr_level) if even else level.append(curr_level[::-1])

            even = not even

        return level
