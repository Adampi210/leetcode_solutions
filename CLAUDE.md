# CLAUDE.md

## Repository Overview

This is a personal collection of Python solutions to LeetCode problems, organized for learning and interview preparation. It also contains a set of algorithm template stubs for common algorithms.

## Directory Structure

```
leetcode_solutions/
├── CLAUDE.md                    # This file
├── README.md                    # Brief repo description
├── solutions/                   # All LeetCode solutions (38 files)
│   └── XXXX_problem_name.py     # Individual solution files
└── useful_algorithms/           # Algorithm reference templates (stubs)
    ├── Sorting/                 # bubble_sort, mergesort, quicksort, selection_sort, treesort, vibe_sort
    ├── graph/                   # Bellman-Ford, Dijkstra, Kruskal
    └── search/                  # bfs, binary_search, dfs
```

## Language and Tooling

- **Language:** Python (exclusively)
- **No build system, test framework, linter, or CI/CD** — solutions are standalone scripts
- **No dependencies** — only Python standard library (`collections.deque` is the most common import)
- **No `.gitignore`** file exists

## File Naming Convention

Solution files follow the pattern: `XXXX_problem_name.py`

- `XXXX` = 4-digit zero-padded LeetCode problem number
- `problem_name` = snake_case description of the problem
- Examples: `0001_two_sum.py`, `0733_flood_fill.py`, `0876_middle_of_linked_list.py`

## Solution File Structure

Each solution file follows a consistent structure:

1. **Problem statement** — comment block at the top describing the problem
2. **Key ideas / algorithm explanation** — comments explaining the approach (labeled `KEY IDEAS:`, `Key insight:`, `SOLUTION:`, or `NOTE:`)
3. **Helper classes** (if needed) — `ListNode`, `TreeNode`, etc., defined inline
4. **Solution class(es)** — one or more classes implementing the solution
5. **Multiple approaches** (optional) — separate classes for different strategies (e.g., `SolutionRecursive`, `SolutionIterative`, `SolutionZip`)

## Code Conventions

### Classes and Methods
- Solution classes inherit from `object` (Python 2 style): `class Solution(object):`
- Method names use camelCase matching LeetCode signatures: `twoSum`, `floodFill`, `climbStairs`
- Multiple solution variants use descriptive class names: `SolutionRecursive`, `SolutionIterative`

### Type Hints
- Docstring-based type hints in LeetCode format:
  ```python
  """
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
  ```

### Variables
- snake_case for all variables: `num_map`, `fast_pointer`, `pixel_val`, `boundary_idx_y`
- Descriptive names preferred over single letters

### Comments
- Extensive inline comments explaining the "why" behind each step
- Algorithm names and techniques are cited (Boyer-Moore, Floyd's cycle detection, etc.)
- Time/space complexity noted where relevant
- Edge cases explicitly called out

### Imports
- Placed where needed (sometimes mid-file, before the class that uses them)
- Most common: `from collections import deque`

## Commit Message Style

Commit messages are brief and reference LeetCode problem numbers:
- `finished 53`
- `finished 104`
- `finish all`
- `did more`
- `added more`

## Guidelines for Adding New Solutions

1. Place the file in `solutions/` with the naming pattern `XXXX_problem_name.py`
2. Start with a comment block containing the problem statement
3. Add a "Key ideas" or "Key insight" comment section explaining the algorithmic approach
4. Define any helper classes (`ListNode`, `TreeNode`) inline in the file
5. Implement the solution in a `Solution(object)` class using LeetCode's method signature
6. Add thorough inline comments explaining each logical step
7. If showing multiple approaches, use separate named classes (e.g., `SolutionRecursive`, `SolutionIterative`)
8. Keep solutions self-contained — no cross-file imports

## Guidelines for Algorithm Templates

- Place template files in the appropriate `useful_algorithms/` subdirectory (`Sorting/`, `graph/`, `search/`)
- Use snake_case or PascalCase filenames matching the algorithm name
- These are currently empty stubs intended to be filled in as reference implementations
