"""
Problem: Minimum Depth of Binary Tree — Given a binary tree, find its minimum depth (number of nodes along the shortest path from root down to nearest leaf node). Key constraints: Node count is in [0, 10^5] and -1000 <= Node.val <= 1000.
Source: LeetCode #111 (https://leetcode.com/problems/minimum-depth-of-binary-tree/)
Solution Pattern: Depth-First Search (Post-order Traversal with Leaf Validation)
Complexity (My Solution):
    - Time: O(N) — In the worst case, visits every node to evaluate path lengths down to leaves.
    - Space: O(H) — Recursion stack depth is proportional to tree height H; O(log N) average, O(N) worst case.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#               2
#             /   \
#          null.   3
#                /   \
#              null.  4
#                    /  \
#                  null  5
#                       /  \
#                     null  6
# A leaf node is the node whose childrens are null
class Solution:
    def helper(self, root):
        if not root:
            return 0

        a = self.helper(root.left)
        b = self.helper(root.right)
        ans = 1

        if a == 0 and b == 0:
            ans = 1
        # If one child is null, minimum depth must be measured along the non-null subtree to a true leaf
        elif a == 0 and b != 0:
            ans = b + 1
        elif a != 0 and b == 0:
            ans = a + 1
        else:
            ans = min(a, b) + 1

        return ans

    def minDepth(self, root: TreeNode | None) -> int:
        return self.helper(root)
