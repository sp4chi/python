# AGENTS.md

## Project Overview

This repository is a personal Python Data Structures & Algorithms (DSA) and LeetCode solution archive. Each `.py` file contains my own implementation of a problem. The primary goal of AI assistance in this repo is to document existing solutions clearly and provide non-destructive code reviews in topic-specific Markdown files without altering my working Python code.

## Core Rules & Boundaries (Never / Always)

### Never

- **NEVER modify, refactor, reformat, or delete existing Python solution code.** Every statement, variable name, import, indentation, type hint, and logic block in my `.py` files must remain identical outside of added docstrings/comments.
- **NEVER guess or fabricate** LeetCode problem numbers, titles, constraints, time/space complexities, or algorithmic patterns. If uncertain about a problem's metadata, verify it against the problem description or official sources, or mark it as `Unknown / Needs Verification`.
- **NEVER overwrite** prior entries in any `REVIEW.md` unless explicitly asked.

### Always

- **ALWAYS preserve original Python logic** when adding explanatory comments or top-level docstrings.
- **ALWAYS verify** edge cases and complexity claims against the actual Python code written in the file (e.g., accounting for list slicing copies, `in` lookups on lists vs. sets, or recursion stack depth).
- **ALWAYS separate feedback from code** by placing Pythonic syntax tips, standard library helpers, and alternative optimal approaches in the respective topic's `REVIEW.md` (e.g., `<topic>/REVIEW.md` like `graphs/REVIEW.md`, `tree/REVIEW.md`, or root `./REVIEW.md` for standalone root-level solutions) rather than editing the `.py` source file.

## Workflow 1: Documenting Python Solution Files

When asked to document or annotate a `.py` solution file, add a structured module-level docstring (`""" ... """`) at the very top of the file—and concise `#` inline comments only where non-obvious logic warrants clarification—using this exact template:

```python
"""
Problem: <Official LeetCode Title> — <1-2 sentence summary of the task and key constraints>
Source: LeetCode #<Number> (<https://leetcode.com<slug>/> if verified)
Solution Pattern: <Algorithmic pattern actually used in my code, e.g., Hash Map Single-Pass, Two Pointers, Sliding Window, Monotonic Stack, DFS/BFS, Dynamic Programming - Tabulation>
Complexity (My Solution):
    - Time: O(...) — <brief reason tied to my loops/operations>
    - Space: O(...) — <brief reason tied to auxiliary data structures/recursion>
"""
```

## Workflow 2: Feedback & Better Solutions (`REVIEW.md` per topic)

Do not edit my `.py` files to apply style fixes or optimizations. Instead, append or update an entry in the respective topic directory's `REVIEW.md` (e.g., `graphs/REVIEW.md`, `tree/REVIEW.md`, or `./REVIEW.md` for files not inside a topic folder) using this structure:

```markdown
## [LeetCode #XXXX] Problem Title (`path/to/solution.py`)

- **Pythonic Syntax & Stdlib Tips:** Cleaner Python idioms, built-ins, or standard library helpers applicable to my code (e.g., `enumerate`, `zip`, `collections.Counter`, `collections.defaultdict`, `collections.deque`, `heapq`, `bisect`, `itertools`, or `math`).
- **Better or Standard Approach:** Name of the canonical/optimal pattern (only if my solution is suboptimal or non-standard), a concise explanation of why it improves time/space complexity, and a short Python reference snippet.
- **Edge Cases to Watch:** Specific Python inputs (e.g., empty list `[]`, single element, negative numbers, duplicates, `None` nodes, or `RecursionError` on deep trees/graphs) that could break or stress the current implementation.
```

## Python Documentation Conventions

- Follow PEP 257 for the top-level module docstring and PEP 8 for `#` inline comments.
- Keep comments concise, objective, and scannable—do not narrate obvious Python syntax line by line.
- Use standard algorithmic terminology (e.g., NeetCode / LeetCode editorial conventions) when naming patterns.

## Verification & Anti-Hallucination Guidelines

- Base all pattern labels and Big-O analyses strictly on the Python operations present in the file (e.g., note that `x in my_list` is $O(n)$ whereas `x in my_set` is $O(1)$ average).
- If a `.py` file does not clearly indicate its LeetCode number or problem statement, inspect the filename, folder path, or existing comments first; if still ambiguous, ask me before writing metadata.
- Do not invent benchmark numbers or claim an alternative is faster without explaining the algorithmic or Python runtime reason.
