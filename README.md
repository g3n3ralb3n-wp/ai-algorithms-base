# AI Algorithms Base Environment

This repository provides a **base Python environment** for the AI Algorithms course. If you're unsure where to start with setting up your development environment, this guide is for you. At the end their are some submission instructions and recommendations when writing out your responses in Jupyter Notebooks.

## What This Is

- A pre-configured environment tested on all homework assignments
- Contains all required dependencies for the course
- Uses **pyenv** for Python version management and **uv** for fast dependency management (a modern alternative to pip and venv)

## Included Reference Codebases

Once you have the environment set up, this repository also includes Python implementations from two well-known algorithm textbooks:

- **[`clrsPython/`](clrsPython/)** — Implementations from *Introduction to Algorithms* (CLRS), 4th Edition, written by Linda Xiao and Tom Cormen
- **[`aima/`](aima/)** — Implementations from *Artificial Intelligence: A Modern Approach* (AIMA), with interactive Jupyter notebooks

These are excellent resources for understanding how the algorithms we cover in class actually work. When you're stuck on an algorithm, look at the reference implementation first — reading real code is often more helpful than asking ChatGPT or Claude, which can hallucinate details or give you subtly incorrect explanations. The textbook code is vetted, matches the pseudocode you'll see in lectures, and will build stronger intuition than an AI-generated summary.

## Important Notes

- **You don't have to use this.** This is just an example to help you get started.
- **You can add to it.** If you need additional packages, feel free to install them.
- **Installation instructions were written by Claude (verified by instructor)** — the Windows instructions may be tricky. I use WSL2 personally and recommend that approach for Windows users.

---

## Installation

### Prerequisites

#### For Windows Users (Recommended: Use WSL2)

Native Windows can be problematic with pyenv. I strongly recommend using **Windows Subsystem for Linux 2 (WSL2)** instead:

- [Install WSL2](https://docs.microsoft.com/en-us/windows/wsl/install)

Once WSL2 is set up, follow the Linux/macOS instructions below from within your WSL2 terminal.

#### For macOS Users

The instructions below should work accurately on macOS.

#### For Linux Users

Follow the instructions below directly.

---

### Step 1: Install pyenv

pyenv allows you to manage multiple Python versions on your system.

**macOS (using Homebrew):**
```bash
brew update
brew install pyenv
```

**Linux/WSL2:**
```bash
curl https://pyenv.run | bash
```

Add pyenv to your shell configuration (`~/.bashrc`, `~/.zshrc`, etc.):
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Restart your terminal or run `source ~/.bashrc` (or `~/.zshrc`).

### Step 2: Install Python 3.13

```bash
pyenv install 3.13
pyenv local 3.13  # Sets Python 3.13 for this project directory
```

Verify:
```bash
python --version  # Should show Python 3.13.x
```

### Step 3: Install uv

uv is a fast Python package installer and resolver (much faster than pip).

**macOS/Linux/WSL2:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Or with Homebrew:**
```bash
brew install uv
```

### Step 4: Create Virtual Environment and Install Dependencies

```bash
uv venv          # Creates a .venv directory
source .venv/bin/activate  # Activate the virtual environment (Linux/macOS/WSL2)
uv sync          # Installs all dependencies from pyproject.toml
```

### Step 5: Verify Installation

Run the included test script to verify all packages are installed correctly:

```bash
python main.py
```

This will test all required packages and display a summary showing which packages were successfully imported along with their versions. You should see output like:

```
AI Algorithms Base Environment - Package Test
------------------------------------------------------------
Testing core scientific packages...
Testing visualization packages...
Testing machine learning packages...
Testing deep learning packages...
Testing reinforcement learning packages...
Testing optimization packages...
Testing dataset packages...
Testing Jupyter packages...

============================================================
PACKAGE TEST RESULTS
============================================================
  numpy         2.x.x                      [OK]
  pandas        2.x.x                      [OK]
  ...
============================================================
Total: 16 | Passed: 16 | Failed: 0
============================================================

All packages installed successfully!
```

If any packages fail to import, the script will indicate which ones need attention.

---

## Workflow: Cloning and Getting Started

If you're new to Git, here's a basic workflow:

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ai-algorithms-base
```

### 2. Set Up the Environment

```bash
pyenv local 3.13
uv venv
source .venv/bin/activate
uv sync
```

### 3. Start Jupyter

```bash
jupyter notebook
# or
jupyter lab
```

### 4. Adding New Packages

If you need additional packages:
```bash
uv add <package-name>
```

---

## Using Markdown Cells (IMPORTANT!)

We expect you to use markdown cells extensively to:

- Explain your thought process
- Describe your approach to solving problems
- Interpret results and findings
- Document assumptions and decisions
- Show mathematical formulas when relevant

### Example Notebook Structure

```
[Markdown Cell]
# Assignment 1: Problem 1
## Understanding the Problem
In this problem, we need to...

[Markdown Cell]
## Approach
I will solve this by:
1. First, ...
2. Then, ...
3. Finally, ...

[Code Cell]
import numpy as np
import pandas as pd
# Your code here

[Markdown Cell]
## Results and Interpretation
The results show that...

[Code Cell]
# Visualization or additional analysis

[Markdown Cell]
## Conclusion
Based on the analysis...
```

### Why Markdown Cells Matter

- They demonstrate your understanding of the concepts
- They show your problem-solving process
- They make your work easier to grade
- They give you practice in technical communication
- They help you organize your thoughts

---

## Best Practices

- **Always execute all cells before submitting** (Kernel → Restart & Run All)
- Clear output and re-run to ensure reproducibility
- Use descriptive variable names
- Comment complex code
- Include visualizations where appropriate
- Explain your results in markdown cells

---

## Organizing Your Work

We recommend this folder structure:

```
base-environment/
├── .venv/                  # Virtual environment (don't commit this)
├── assignment-1/
│   ├── assignment-1.ipynb  # Your notebook
│   ├── assignment-1.html   # Exported HTML
│   └── data/               # Any data files (if needed)
├── assignment-2/
│   ├── assignment-2.ipynb
│   └── assignment-2.pdf
├── project/
│   └── ...
├── pyproject.toml
├── README.md
└── main.py
```

---

## Submission Requirements

For each assignment, you must submit:

### 1. Fully Executed Jupyter Notebook (.ipynb)

- All cells must be executed
- All output must be visible
- Include both code and markdown cells

To ensure your notebook is fully executed:
1. **Kernel → Restart & Run All**
2. Then save the notebook (Ctrl+S or Cmd+S)

### 2. Exported Version (HTML or PDF)

You must also submit an exported version for easy viewing in Canvas.

#### Option A: Export to HTML (Recommended)

**From Jupyter Notebook/Lab:**
- File → Download as → HTML (.html)

**From command line:**
```bash
jupyter nbconvert --to html assignment-1.ipynb
```

#### Option B: Export to PDF

**From Jupyter (requires additional setup):**
- File → Download as → PDF via LaTeX (.pdf)

**From command line:**
```bash
# First, ensure you have nbconvert and pandoc installed
uv add nbconvert
# Install pandoc: https://pandoc.org/installing.html

jupyter nbconvert --to pdf assignment-1.ipynb
```

**Alternative (HTML → PDF):**
1. Export to HTML first
2. Open the HTML file in your browser
3. Print to PDF (Ctrl+P / Cmd+P → Save as PDF)

### What to Submit to Canvas

Upload **both** files:
1. `assignment-X.ipynb` (the notebook file)
2. `assignment-X.html` or `assignment-X.pdf` (the exported version)

The exported version ensures we can view your work even if there are compatibility issues with the notebook.

---

## Included Packages

This environment includes:

| Package | Purpose |
|---------|---------|
| numpy | Numerical computing |
| pandas | Data manipulation |
| matplotlib | Plotting |
| seaborn | Statistical visualization |
| scikit-learn | Machine learning |
| torch | Deep learning (PyTorch) |
| torchvision | Computer vision utilities |
| transformers | Hugging Face models |
| gymnasium | Reinforcement learning environments |
| networkx | Graph algorithms |
| ortools | Optimization (Google OR-Tools) |
| pyswarms | Particle swarm optimization |
| scipy | Scientific computing |
| datasets | Hugging Face datasets |
| jupyter | Jupyter notebooks |

---

## Troubleshooting

**pyenv not found after installation:**
- Make sure you added pyenv to your shell configuration and restarted your terminal

**uv command not found:**
- Restart your terminal after installing uv

**Python version mismatch:**
- Run `pyenv local 3.13` in the project directory

**Package import errors:**
- Make sure your virtual environment is activated: `source .venv/bin/activate`
- Run `uv sync` to ensure all packages are installed

---

## Questions?

If you have questions about the environment setup, please ask during office hours or post on the course discussion board.
