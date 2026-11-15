"""
Problem: Flatten Binary Tree to Linked List — Given the root of a binary tree, flatten the tree into a "linked list" in-place following pre-order traversal using right child pointers. Key constraints: Node count is in [0, 2000] and -100 <= Node.val <= 100.
Source: LeetCode #114 (https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
Solution Pattern: Reverse Post-order Traversal (DFS / Right-Left-Root Traversal)
Complexity (My Solution):
    - Time: O(N) — Every node is visited during post-order in-place pointer updates.
    - Space: O(H) — Call stack depth corresponds to tree height H; O(log N) for balanced trees, O(N) for degenerate trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None

        def helper_post(root):

            nonlocal prev

            # no subtree
            if not root:
                return None

            helper_post(root.right)
            helper_post(root.left)

            # Reverse post-order (Right -> Left -> Root) links current node to previously processed node
            root.right = prev
            root.left = None
            prev = root
            # if root.left:
            #     root.right = root.left
            #     root.left = None
            #     b.right = a

        helper_post(root)

        def helper_pre(root):

            # no subtree
            if not root:
                return None

            right = root.right

            a = helper_post(root.left)  # 4
            b = helper_post(root.right)  # 6

            if root.left:
                root.right = root.left
                root.left = None
                a.right = right
            return b or a or root

        helper_pre(root)
