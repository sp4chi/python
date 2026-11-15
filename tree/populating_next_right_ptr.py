"""
Problem: Populating Next Right Pointers in Each Node — Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL. Key constraints: Perfect binary tree with node count in [0, 2^12 - 1] and -1000 <= Node.val <= 1000.
Source: LeetCode #116 (https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)
Solution Pattern: Breadth-First Search (Level-Order Traversal with Queue)
Complexity (My Solution):
    - Time: O(N) — Every node is popped and its next pointer assigned once.
    - Space: O(N) — Queue holds up to N/2 leaf nodes at the bottom level of the perfect binary tree.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# leetcode - 116


class Solution:
    def connect(self, root):
        if not root:
            return None
        q = deque([root])
        while q:
            rightNode = None
            for _ in range(len(q)):
                cur = q.popleft()
                # Right-to-left traversal at current level links cur.next to previously popped node
                cur.next, rightNode = rightNode, cur
                if cur.right:
                    q.extend([cur.right, cur.left])
        return root
