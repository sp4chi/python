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
