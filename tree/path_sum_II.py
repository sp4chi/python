"""
Problem: Path Sum II — Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Key constraints: Node count is in [0, 5000], -1000 <= Node.val <= 1000, and -1000 <= targetSum <= 1000.
Source: LeetCode #113 (https://leetcode.com/problems/path-sum-ii/)
Solution Pattern: Backtracking (DFS Pre-order Traversal)
Complexity (My Solution):
    - Time: O(N^2) — In the worst case (full tree matching target at all leaves), copying paths takes O(N) time for O(N) leaves.
    - Space: O(H) — Auxiliary call stack and temp path list require O(H) space, excluding returned output paths.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        main = []
        temp = []

        def helper(node, remaining):
            # empty subtree
            if not node:
                return

            remaining -= node.val
            temp.append(node.val)

            # leaf node
            if not node.left and not node.right:
                if remaining == 0:
                    main.append(temp[:])
            # not a leaf
            else:
                helper(node.left, remaining)
                helper(node.right, remaining)
            # Backtrack by removing current node before returning up the call stack
            temp.pop()

        helper(root, targetSum)
        return main
