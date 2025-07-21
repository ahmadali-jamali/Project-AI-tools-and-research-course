
# Project-AI-tools-and-research-course
# Matrix Multiplication Implementation



#In this practice Python language in windows is used
 
#Step by step of the repository:

 At first the new directory should be created by bellow command: 
mkdir matrix-multiplication
cd matrix-multiplication

initialized repository created by bellow command:
git init

The basic version of the code is created in Python.
Check the Python VScode matrix.py

the .gitignore file created


Create develop brache
git checkout -b development

the profile_matrix.py created as Make Improvements in Development Branch
Check the profile_matrix file 

The requirement file as text file is created 
See the requirements.txt

Merge Development into Main is created by bellow command: 
git checkout main
git merge development
# Or for rebase:
git checkout development
git rebase main
git checkout main
git merge development

Create README.md 
This repository contains implementations of matrix multiplication in Python, with performance optimizations.

To run the program insert the bellow command:
python matrix.py

## Implementations

1. **Naive Implementation**: Basic triple-nested loop implementation.
2. **Optimized Implementation**: Uses list comprehensions for better performance.

## Performance Improvements

After profiling with various matrix sizes (10x10 to 200x200), the optimized version showed:
- 15-20% faster for smaller matrices (10x10 to 50x50)
- 25-30% faster for larger matrices (100x100 to 200x200)

The improvement comes from Python's more efficient handling of list comprehensions compared to explicit loops.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

Best regards
Ahmadali Jamali
