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
            lvl.append(curr_lvl[-1])
        return lvl
