# Code Reviews

## [LeetCode #530] Minimum Absolute Difference in BST (`tree/min_distance_bst.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **Unused Import:** `from collections import deque` is imported at module level but only used in commented-out scratch code. Removing unused imports keeps the module namespace clean.
  - **Type Annotations:** `root: Optional[TreeNode]` requires `from typing import Optional` (or in Python 3.10+, `TreeNode | None`). Without importing `Optional`, running the script directly raises a `NameError` unless evaluated under `from __future__ import annotations`.
  - **Base Case Return Value:** In `dfs(node)`, the base condition returns `float("inf")` (`if not node: return float("inf")`), but recursive invocations (`dfs(node.left)`) discard the return value. Using a bare `return` or returning `None` makes it explicit that `dfs` is a void traversal function relying on closure side effects (`nonlocal md, prev`).
  - **Generator Traversal with `itertools.pairwise`:** In Python 3.10+, an in-order generator paired with `itertools.pairwise` separates tree traversal from difference tracking cleanly:
    ```python
    from itertools import pairwise
    from typing import Iterator, Optional

    class Solution:
        def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
            def inorder(node: Optional[TreeNode]) -> Iterator[int]:
                if node:
                    yield from inorder(node.left)
                    yield node.val
                    yield from inorder(node.right)

            return min(b - a for a, b in pairwise(inorder(root)))
    ```

- **Better or Standard Approach:**
  - **Iterative In-Order Traversal (Explicit Stack):** Your recursive in-order traversal is already time-optimal at $O(N)$ and space-optimal at $O(H)$ auxiliary space. However, Python enforces a default recursion limit of 1,000 frames (`sys.getrecursionlimit()`). On degenerate or heavily skewed trees ($N = 10^4$), recursion can raise a `RecursionError`. An iterative in-order traversal replaces the call stack with a heap-allocated Python list, avoiding recursion depth limits while maintaining $O(N)$ time and $O(H)$ space:
    ```python
    class Solution:
        def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
            stack = []
            curr = root
            prev = None
            min_diff = float("inf")

            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()

                if prev is not None:
                    min_diff = min(min_diff, curr.val - prev)
                prev = curr.val

                curr = curr.right

            return int(min_diff)
    ```

- **Edge Cases to Watch:**
  - **Deep / Skewed BST (Recursion Limit):** Trees structured like linked lists with $N > 1,000$ will crash with `RecursionError: maximum recursion depth exceeded`.
  - **Minimum Number of Nodes ($N = 2$):** The problem guarantees $N \ge 2$, ensuring `prev` is always set before comparing adjacent values. If run on a tree with fewer than 2 nodes, `md` would remain `float("inf")`.
  - **Duplicate Values:** Although BST definitions usually enforce unique keys, if duplicate values were permitted, `node.val - prev` evaluates to `0`, which is handled correctly.

## [LeetCode #108] Convert Sorted Array to Binary Search Tree (`tree/balance_tree.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **Type Annotations:** `helper` uses `List[int]` which is not imported; in modern Python (3.9+), use built-in `list[int]` as done in `sortedArrayToBST`.
  - **Middle Calculation:** In Python, arbitrary-precision integers avoid integer overflow, so `mid = (left + right) // 2` is standard and more readable than `left + (right - left) // 2`.
  - **Inner Helper (Closure):** Defining `helper` inside `sortedArrayToBST` avoids passing `nums` repeatedly through every recursive frame.
- **Better or Standard Approach:**
  - Divide and Conquer using indices is the optimal pattern ($O(N)$ time, $O(\log N)$ auxiliary space). Slicing `nums[:mid]` and `nums[mid+1:]` is common for Python one-liners, but passing boundary indices (as in your code) is superior because array slicing creates $O(N)$ copy overhead per level.
    ```python
    class Solution:
        def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
            def build(left: int, right: int) -> TreeNode | None:
                if left > right:
                    return None
                mid = (left + right) // 2
                return TreeNode(
                    nums[mid],
                    build(left, mid - 1),
                    build(mid + 1, right)
                )

            return build(0, len(nums) - 1)
    ```
- **Edge Cases to Watch:**
  - **Empty List `nums = []`:** `len(nums) - 1` evaluates to `-1`, triggering `left > right` and returning `None` safely.
  - **Single Element `[x]`:** Correctly produces a single root node with `left=None` and `right=None`.
  - **Even Length Array:** Both lower-mid `(left + right) // 2` and upper-mid `(left + right + 1) // 2` yield valid height-balanced BSTs.

## [LeetCode #110] Balanced Binary Tree (`tree/balanced_binary_tree.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **Duplicate Method Definition:** `def isBalanced` is declared twice in `Solution`. In Python, the second definition unconditionally overrides the first in the class dictionary at import/runtime.
  - **Boolean Return Value:** Approach 1 returns `1 if balance else 0` (integers `1` or `0`), but the LeetCode method signature expects a `bool`.
  - **Descriptive Variable Names:** In Approach 1, parameter `A` should be renamed `root: TreeNode | None` to conform with PEP 8 and standard tree conventions.
- **Better or Standard Approach:**
  - **Bottom-Up Post-Order DFS with Sentinel (`-1`):** Approach 2 is the canonical optimal pattern. Returning `-1` as soon as any child subtree is unbalanced short-circuits unnecessary depth calculations, running in $O(N)$ time and $O(H)$ space:
    ```python
    class Solution:
        def isBalanced(self, root: TreeNode | None) -> bool:
            def get_height(node: TreeNode | None) -> int:
                if not node:
                    return 0
                left, right = get_height(node.left), get_height(node.right)
                if left == -1 or right == -1 or abs(left - right) > 1:
                    return -1
                return max(left, right) + 1

            return get_height(root) != -1
    ```
- **Edge Cases to Watch:**
  - **Empty Tree `root = None`:** Trivially balanced; returns `True`.
  - **Heavily Skewed Tree ($N = 5000$):** Can exceed Python's recursion limit (`sys.getrecursionlimit()`).
  - **Imbalance at Deep Subtree:** Handled in $O(N)$ because the sentinel `-1` propagates immediately up to the root.

## [LeetCode #543] Diameter of Binary Tree (`tree/diameter_of_bst.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **Misleading Filename:** The problem is for a general Binary Tree (LeetCode #543), not a Binary Search Tree (BST).
  - **Unused Class Attribute:** `d = -1` defined at the class level is shadowed by the inner local variable `d = -1` and `nonlocal d`, leaving the class attribute unused.
  - **Missing Type Import:** `root: Optional[TreeNode]` requires `from typing import Optional` or modern union `TreeNode | None`.
- **Better or Standard Approach:**
  - Post-order DFS is already the canonical optimal pattern ($O(N)$ time, $O(H)$ space). Wrapping the traversal inside an inner function that tracks diameter via a closure variable is clean:
    ```python
    class Solution:
        def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
            diameter = 0

            def max_depth(node: TreeNode | None) -> int:
                nonlocal diameter
                if not node:
                    return 0
                left, right = max_depth(node.left), max_depth(node.right)
                diameter = max(diameter, left + right)
                return max(left, right) + 1

            max_depth(root)
            return diameter
    ```
- **Edge Cases to Watch:**
  - **Single Node Tree:** The diameter in edges is `0`. Initializing `diameter = 0` (or `d = -1` with `d = max(d, 0 + 0)`) handles this correctly.
  - **Diameter Not Passing Through Root:** When one subtree is much wider and deeper than the other, the longest path does not include the root node; calculating `max(d, a + b)` at every node properly captures this.

## [LeetCode #114] Flatten Binary Tree to Linked List (`tree/flatten_binary_tree.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **Redundant Function Calls:** `helper_post(root)` completely flattens the tree in reverse post-order. However, `helper_pre(root)` is also invoked immediately afterwards, performing redundant node rewiring. Calling only `helper_post(root)` is sufficient.
  - **Dead Code:** Commented-out lines inside `helper_post` can be removed to improve clarity.
- **Better or Standard Approach:**
  - **Morris Traversal ($O(1)$ Space):** While reverse post-order recursion runs in $O(N)$ time and $O(H)$ space, Morris Traversal can flatten the tree in-place in $O(N)$ time with $O(1)$ auxiliary space without any recursion stack:
    ```python
    class Solution:
        def flatten(self, root: TreeNode | None) -> None:
            curr = root
            while curr:
                if curr.left:
                    # Find predecessor (rightmost node in left subtree)
                    pred = curr.left
                    while pred.right:
                        pred = pred.right
                    pred.right = curr.right
                    curr.right = curr.left
                    curr.left = None
                curr = curr.right
    ```
- **Edge Cases to Watch:**
  - **Empty Tree `root = None`:** Returns `None` immediately without mutation.
  - **Already Flattened Right-Skewed Tree:** Traverses without performing any unnecessary pointer modifications.
  - **Left-Skewed Tree:** Successfully moves all left children into right linked pointers.

## [LeetCode #94] Binary Tree Inorder Traversal (`tree/inorderTraversal.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **PEP 8 Identity Check:** Use `if root is None:` instead of `if root == None:`.
  - **Variable Naming:** Avoid single-letter variable names like `l` which can easily be misread as `1` or `I`; prefer `result` or `res`.
  - **Generator Function:** Rather than passing an accumulator list through recursive calls, use Python's generator delegation `yield from`:
    ```python
    class Solution:
        def inorderTraversal(self, root: TreeNode | None) -> list[int]:
            def inorder(node: TreeNode | None):
                if node:
                    yield from inorder(node.left)
                    yield node.val
                    yield from inorder(node.right)

            return list(inorder(root))
    ```
- **Better or Standard Approach:**
  - **Iterative Traversal with Explicit Stack:** Avoids call stack frames and `RecursionError` on deep trees ($O(N)$ time, $O(H)$ space):
    ```python
    class Solution:
        def inorderTraversal(self, root: TreeNode | None) -> list[int]:
            res, stack = [], []
            curr = root
            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
            return res
    ```
- **Edge Cases to Watch:**
  - **Empty Tree `root = None`:** Returns `[]`.
  - **Skewed Trees:** Deep single-branch trees can stress call stack limits; iterative stack avoids this.

## [LeetCode #226] Invert Binary Tree (`tree/invert_binary_tree.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - The simultaneous tuple assignment `root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)` is exceptionally concise and idiomatic Python.
- **Better or Standard Approach:**
  - **Iterative BFS / Queue:** Your recursive DFS is $O(N)$ time and $O(H)$ space. For trees with large depths, an iterative BFS level-order swap eliminates call stack overhead:
    ```python
    from collections import deque

    class Solution:
        def invertTree(self, root: TreeNode | None) -> TreeNode | None:
            if not root:
                return None
            queue = deque([root])
            while queue:
                node = queue.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return root
    ```
- **Edge Cases to Watch:**
  - **Empty Tree `root = None`:** Returns `None`.
  - **Single Node Tree:** Returns node unchanged with children `None`.

## [LeetCode #236] Lowest Common Ancestor of a Binary Tree (`tree/lca.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **Object Identity:** Comparing `path_p[i].val == path_q[i].val` assumes all node values are unique. In general tree problems or object graphs, check object identity `path_p[i] is path_q[i]`.
  - **Comparing Paths with `zip`:** The while loop comparing path elements can be written concisely with `zip`:
    ```python
    lca = root
    for u, v in zip(path_p, path_q):
        if u is v:
            lca = u
        else:
            break
    ```
- **Better or Standard Approach:**
  - **Single-Pass Post-Order DFS (No Path Storage):** Instead of storing and reversing two explicit path lists, the canonical recursive LCA algorithm returns the target node when found and the current root when `left` and `right` subtrees both return non-null. This cuts auxiliary space from $O(H)$ path storage to $O(1)$ auxiliary (excluding call stack):
    ```python
    class Solution:
        def lowestCommonAncestor(
            self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
        ) -> 'TreeNode':
            if not root or root is p or root is q:
                return root
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            return root if left and right else (left or right)
    ```
- **Edge Cases to Watch:**
  - **`p` is Ancestor of `q` (or vice-versa):** Both approaches correctly return `p` as the LCA.
  - **Large Trees ($N = 10^5$):** Single-pass DFS is significantly faster and uses less memory because it does not allocate path lists.

## [LeetCode #107] Binary Tree Level Order Traversal II (`tree/level_order_bottom_up.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **Double-Ended Queue for Output:** Instead of `level.append(curr_lvl)` followed by `level.reverse()`, you can use `collections.deque` and call `level.appendleft(curr_lvl)`.
  - **Direct Deque Initialization:** Replace `queue = deque(); queue.append(root)` with `queue = deque([root])`.
- **Better or Standard Approach:**
  - BFS with a queue is the standard optimal approach ($O(N)$ time, $O(W)$ space). Batch-level list comprehensions provide a clean, Pythonic structure:
    ```python
    from collections import deque

    class Solution:
        def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
            if not root:
                return []
            res = deque()
            level = [root]
            while level:
                res.appendleft([n.val for n in level])
                level = [c for n in level for c in (n.left, n.right) if c]
            return list(res)
    ```
- **Edge Cases to Watch:**
  - **Empty Tree `root = None`:** Returns `[]`.
  - **Single Node Tree:** Returns `[[val]]`.

## [LeetCode #102] Binary Tree Level Order Traversal (`tree/level_order.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **Direct Child Enqueuing:** Avoid temporary variables `left` and `right` by appending directly:
    ```python
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
    ```
  - **Queue Initialization:** Initialize directly with `queue = deque([root])`.
- **Better or Standard Approach:**
  - Canonical queue BFS is already optimal ($O(N)$ time, $O(W)$ space). A batch comprehension approach:
    ```python
    class Solution:
        def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
            if not root:
                return []
            res, level = [], [root]
            while level:
                res.append([n.val for n in level])
                level = [c for n in level for c in (n.left, n.right) if c]
            return res
    ```
- **Edge Cases to Watch:**
  - **Empty Tree `root = None`:** Handled by early guard returning `[]`.
  - **Skewed vs Complete Trees:** For skewed trees, maximum queue size is 1 ($O(1)$ space); for complete trees, maximum queue size is $N/2$ ($O(N)$ space).

## [LeetCode #104] Maximum Depth of Binary Tree (`tree/max_depth.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - Concise ternary expression:
    ```python
    class Solution:
        def maxDepth(self, root: TreeNode | None) -> int:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
    ```
- **Better or Standard Approach:**
  - **Iterative BFS for Deep Trees:** Recursive DFS is $O(N)$ time and $O(H)$ space. For degenerate trees where $N = 10^4$, a queue-based level traversal increments a depth counter per level, avoiding Python recursion limit exceptions:
    ```python
    from collections import deque

    class Solution:
        def maxDepth(self, root: TreeNode | None) -> int:
            if not root:
                return 0
            queue, depth = deque([root]), 0
            while queue:
                depth += 1
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return depth
    ```
- **Edge Cases to Watch:**
  - **Empty Tree `root = None`:** Returns `0`.
  - **Single Node Tree:** Returns `1`.

## [LeetCode #111] Minimum Depth of Binary Tree (`tree/min_depth.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **Branch Simplification:** The four-way `if/elif/else` in `helper` can be simplified: if either child is null, the minimum depth is `max(a, b) + 1` (or `a + b + 1`); if both exist, it is `min(a, b) + 1`.
  - The separate `helper` method is unnecessary if `minDepth` handles base conditions directly.
- **Better or Standard Approach:**
  - **Early-Exit BFS (Optimal Time):** DFS must traverse every node in the worst case ($O(N)$) even if a leaf exists at depth 2 while another branch is $10^5$ deep. BFS checks level by level and terminates immediately when the *first* leaf is encountered ($O(K)$ time where $K \le N$):
    ```python
    from collections import deque

    class Solution:
        def minDepth(self, root: TreeNode | None) -> int:
            if not root:
                return 0
            queue = deque([(root, 1)])
            while queue:
                node, depth = queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append((node.left, depth + 1))
                if node.right:
                    queue.append((node.right, depth + 1))
    ```
- **Edge Cases to Watch:**
  - **Skewed Tree (Node with Only One Child):** A node with one null child is not a leaf; the path must continue down to an actual leaf. Your logic correctly accounts for this.
  - **Empty Tree:** Returns `0`.

## [LeetCode #113] Path Sum II (`tree/path_sum_II.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **Path Copying:** `temp[:]` creates a shallow slice copy, which is necessary to avoid mutating stored paths. `temp.copy()` or `list(temp)` is equally clear.
  - **Variable Naming:** Rename `main` to `result` or `paths` for better self-documentation.
- **Better or Standard Approach:**
  - Your backtracking approach with `temp.append()` and `temp.pop()` is the standard optimal pattern because it maintains a single auxiliary list rather than creating intermediate list copies at every tree node.
  - An iterative DFS using a stack storing `(node, remaining, path)` can be used if call stack depth is a constraint.
- **Edge Cases to Watch:**
  - **Negative Values:** Node values and target sums can be negative (`-1000 <= val <= 1000`). Traversal cannot be pruned early when the sum exceeds `targetSum`.
  - **Leaf with Value 0:** Properly handled when `not node.left and not node.right and remaining == 0`.
  - **Empty Tree `root = None`:** Returns `[]`.

## [LeetCode #116] Populating Next Right Pointers in Each Node (`tree/populating_next_right_ptr.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **Missing Import:** `deque` is used in `connect` without `from collections import deque`.
  - Type annotations on `Node` methods can leverage `from __future__ import annotations`.
- **Better or Standard Approach:**
  - **$O(1)$ Auxiliary Space Pointer Linking (Canonical Optimal):** Because the tree is a *perfect* binary tree, you can use the already populated `.next` pointers of level $N$ to establish the `.next` pointers of level $N+1$, eliminating the queue entirely:
    ```python
    class Solution:
        def connect(self, root: 'Node | None') -> 'Node | None':
            leftmost = root
            while leftmost and leftmost.left:
                curr = leftmost
                while curr:
                    # Connect left child to right child
                    curr.left.next = curr.right
                    # Connect right child to next subtree's left child
                    if curr.next:
                        curr.right.next = curr.next.left
                    curr = curr.next
                leftmost = leftmost.left
            return root
    ```
- **Edge Cases to Watch:**
  - **Empty Tree `root = None`:** Returns `None`.
  - **Single Node Tree:** Has no children; loop terminates and returns `root` with `root.next = None`.

## [LeetCode #257] Binary Tree Paths (`tree/print_all_paths.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **Redundant Base Case:** The check `if not root.left and not root.right: l.append(str(root.val)); return l` duplicates the leaf logic inside `paths()`. Invoking `paths(root, path)` directly handles single-node trees cleanly.
  - **Immutable Path Arguments:** Passing `path + "->" + str(node.val)` avoids mutable list state and removes the need for explicit `path.pop()`.
- **Better or Standard Approach:**
  - Backtracking with `path.pop()` avoids intermediate string allocations during traversal. Alternatively, recursive DFS appending formatted path strings:
    ```python
    class Solution:
        def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
            paths = []

            def dfs(node: TreeNode | None, current_path: str):
                if node:
                    current_path += str(node.val)
                    if not node.left and not node.right:
                        paths.append(current_path)
                    else:
                        current_path += "->"
                        dfs(node.left, current_path)
                        dfs(node.right, current_path)

            dfs(root, "")
            return paths
    ```
- **Edge Cases to Watch:**
  - **Single Node Tree:** Returns `["val"]` without trailing arrows.
  - **Negative Values:** Converted properly to strings (e.g. `"-1->-2"`).

## [LeetCode #199] Binary Tree Right Side View (`tree/right_side_view.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **Unnecessary List Allocations:** `curr_lvl` stores every node's value at each level, only for `lvl.append(curr_lvl[-1])` to keep the last element. Only append when `i == size - 1` to conserve memory:
    ```python
    if i == size - 1:
        lvl.append(node.val)
    ```
- **Better or Standard Approach:**
  - **Recursive DFS (Right-First Traversal):** Traverses right child before left child. If current recursion depth equals `len(res)`, the current node is the rightmost visible node at this depth, achieving $O(H)$ auxiliary space without queue overhead:
    ```python
    class Solution:
        def rightSideView(self, root: TreeNode | None) -> list[int]:
            res = []

            def dfs(node: TreeNode | None, depth: int):
                if not node:
                    return
                if depth == len(res):
                    res.append(node.val)
                dfs(node.right, depth + 1)
                dfs(node.left, depth + 1)

            dfs(root, 0)
            return res
    ```
- **Edge Cases to Watch:**
  - **Left-Skewed Tree:** Even though nodes are left children, they are visible from the right if nothing obscures them; both BFS and right-first DFS handle this correctly.
  - **Empty Tree `root = None`:** Returns `[]`.

## [LeetCode #100] Same Tree (`tree/same_tree.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - Consolidate null checks:
    ```python
    if not p or not q:
        return p == q
    ```
  - Concise expression:
    ```python
    class Solution:
        def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
            if not p or not q:
                return p == q
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    ```
- **Better or Standard Approach:**
  - Your recursive DFS is the canonical optimal solution ($O(N)$ time, $O(H)$ space). An iterative queue check with `deque([(p, q)])` is standard when call stack depth is constrained.
- **Edge Cases to Watch:**
  - **Both Trees Empty:** Returns `True`.
  - **One Tree Empty, One Non-Empty:** Returns `False`.
  - **Identical Structure but Different Values:** Caught immediately by value comparison.

## [LeetCode #101] Symmetric Tree (`tree/symmetricTree.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **PEP 8 Identity Comparison:** Replace `if root == None:` with `if root is None:`.
  - Combine base checks:
    ```python
    if not leftTree or not rightTree:
        return leftTree == rightTree
    ```
- **Better or Standard Approach:**
  - **Iterative Queue Mirror Check:** While recursive mirror DFS is canonical, an iterative queue version verifies symmetry level-by-level without recursion depth risks:
    ```python
    from collections import deque

    class Solution:
        def isSymmetric(self, root: TreeNode | None) -> bool:
            if not root:
                return True
            queue = deque([(root.left, root.right)])
            while queue:
                t1, t2 = queue.popleft()
                if not t1 and not t2:
                    continue
                if not t1 or not t2 or t1.val != t2.val:
                    return False
                queue.append((t1.left, t2.right))
                queue.append((t1.right, t2.left))
            return True
    ```
- **Edge Cases to Watch:**
  - **Single Node Tree:** Symmetric with itself; returns `True`.
  - **Asymmetric Structure with Matching Values:** Handled correctly by mirror child pairings `(t1.left, t2.right)` and `(t1.right, t2.left)`.

## [LeetCode #98] Validate Binary Search Tree (`tree/valid_bst.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - The chained comparison `min_bound < root.val < max_bound` is clean and idiomatic in Python.
  - Floating point bounds `float('-inf')` and `float('inf')` work cleanly for standard Python comparisons.
- **Better or Standard Approach:**
  - **In-Order Traversal with Previous Value Tracking:** In a valid BST, an in-order traversal visits nodes in strictly monotonically increasing order. Tracking `prev` iteratively with a stack avoids recursion limits:
    ```python
    class Solution:
        def isValidBST(self, root: TreeNode | None) -> bool:
            stack = []
            curr = root
            prev = float("-inf")
            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()
                if curr.val <= prev:
                    return False
                prev = curr.val
                curr = curr.right
            return True
    ```
- **Edge Cases to Watch:**
  - **Duplicate Values:** BSTs strictly require `left < root < right`. Nodes with equal values return `False`.
  - **Integer Boundary Collisions:** Values equal to `2^31 - 1` or `-2^31` are handled safely by using `float('-inf')` and `float('inf')`.

## [LeetCode #103] Binary Tree Zigzag Level Order Traversal (`tree/zigzag_order.py`)

- **Pythonic Syntax & Stdlib Tips:**
  - **Conditional Statement vs Expression:** `level.append(curr_level) if even else level.append(curr_level[::-1])` duplicates `level.append`. Idiomatic Python:
    ```python
    level.append(curr_level if even else curr_level[::-1])
    ```
  - **Double-Ended Queue per Level:** Instead of reversing `curr_level[::-1]` at odd depths, construct each level using `deque()` and use `append` or `appendleft` based on `even`.
- **Better or Standard Approach:**
  - Using a deque for `curr_level` avoids the $O(K)$ array reversal and slice copy:
    ```python
    from collections import deque

    class Solution:
        def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
            if not root:
                return []
            res = []
            queue = deque([root])
            left_to_right = True

            while queue:
                level = deque()
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if left_to_right:
                        level.append(node.val)
                    else:
                        level.appendleft(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res.append(list(level))
                left_to_right = not left_to_right

            return res
    ```
- **Edge Cases to Watch:**
  - **Empty Tree `root = None`:** Returns `[]`.
  - **Single Node Tree:** Returns `[[val]]` without reversing.\n