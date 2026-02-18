# CLRS Python - AI Algorithms Course Reference

This folder contains Python implementations of algorithms from **Introduction to Algorithms, Fourth Edition** (CLRS) by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. It has been included as part of the **AI Algorithms Base Environment** to give you direct access to textbook algorithm implementations alongside your course assignments.

## How This Fits Into the Course

The parent project (`ai-algorithms-base`) provides your development environment, dependencies, and assignment workflow. This `clrsPython/` folder supplements that with reference implementations organized by textbook chapter. You can:

- **Study the implementations** of foundational algorithms covered in lectures (sorting, graph algorithms, dynamic programming, greedy algorithms, etc.)
- **Reference the code** when working on assignments that build on CLRS algorithms
- **Compare pseudocode to Python** — the implementations closely follow the pseudocode in the book

For environment setup, dependencies, and assignment submission instructions, refer to the [main project README](../README.md).

## Chapter Contents

The implementations are organized by chapter, covering topics including:

| Chapters | Topics |
|----------|--------|
| 2, 4–9 | Sorting and order statistics |
| 10–14 | Data structures (linked lists, hash tables, BSTs, red-black trees, augmenting) |
| 15–16 | Dynamic programming and greedy algorithms |
| 17 | Amortized analysis |
| 18–19 | Advanced data structures (B-trees, Fibonacci heaps) |
| 20–21 | van Emde Boas trees, disjoint sets |
| 22–25 | Graph algorithms (BFS, DFS, MST, shortest paths, all-pairs shortest paths) |
| 28 | Matrix operations |
| 30–32 | Polynomials/FFT, number theory, string matching |
| 35 | Approximation algorithms |

A `Utility functions` folder contains shared helper code used across chapters.

## Setup: Fixing Cross-Chapter Imports

Many of the CLRS Python files import from other chapters (e.g., Chapter 22's Dijkstra imports from Chapter 10's min-heap). By default Python won't know where to find these, so you'll get `ModuleNotFoundError` when trying to run them.

To fix this, **activate your virtual environment** and run the included setup script from the project root:

```bash
source .venv/bin/activate
python clrsPython/setup_paths.py
```

This creates a `clrs_paths.pth` file in your virtual environment's `site-packages/` that registers every chapter folder on Python's import path. You only need to run it once — the paths will persist for the lifetime of the virtual environment.

If you ever recreate your `.venv`, just run the script again.

---

## Original Authors' Note

This Python code was written by Linda Xiao and Tom Cormen. It is provided for reference and closely matches the pseudocode in the book, though the authors have varied from the book's implementation where they saw fit. The code has been minimally tested — if you plan to use it in your own codebase, you should test it further and observe the MIT License included in each Python file within this folder.

If you find an error in this Python code, please report it to Tom Cormen, thc@cs.dartmouth.edu.
