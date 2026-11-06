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
