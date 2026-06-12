# Word Frequency Analyzer

## Description 
This is a command line tool that analyzes data (primarily words) from a text file (.txt) and checks how many times a word occurs or repeats in that file.

**Requirements:**
- **Python:**: Python 3.7+

**Usage:**
- **Run:**: Execute the analyzer with `python main.py` from the project root. The script reads `data.txt` by default.


**Input Format:**
- **File:**: Provide a plain text file named `data.txt` in the project root (words can be separated by spaces and/or newlines).

**Example:**
- **Sample file:**: `data.txt` containing words (one per line or space-separated).
- **Output:**: The script prints a line like `Top most common word is apple with a count of 12`.


**Notes & Limitations:**
- **Normalization:**: Words are not lowercased or stripped of punctuation — add preprocessing if needed.
- **File name:**: `main.py` uses `data.txt` specifically; rename or modify the script to accept command-line paths.



