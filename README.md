# word-frequency-hash-table
Python word frequency counter comparing hash table O(1) vs list O(n) performance on Adventures of Huckleberry Finn — includes bigram analysis

# Word Frequency Counter — Hash Table vs List
### Python | Data Structures | Algorithms

## What This Project Does
This script reads the full text of Adventures of Huckleberry Finn and 
counts how often each word appears. It also finds the most common 
two-word combinations in the book.

The main goal was to compare two ways of counting words and see which 
one is faster:
- Dictionary (hash table) — fast
- List — slow

## Results
- Read and processed 110,000+ words from the full book
- Found the top 20 most frequent words
- Found the top 10 most frequent word pairs
- The dictionary method was much faster than the list method

## How It Works

**Read the file**
Tries three different text encodings until the file opens successfully.

**Clean the text**
Converts all text to lowercase and removes punctuation so "The" and 
"the" are counted as the same word.

**Count words two ways**
The dictionary method looks up each word instantly — it does not matter 
how many words are in the dictionary, it always takes the same time.

The list method scans from the beginning every time it looks for a word. 
The longer the list gets, the slower it becomes.

**Word pairs**
The script also counts pairs of words that appear next to each other, 
like "Tom Sawyer" or "old man".

**Output**
Prints a table of the top 20 words and top 10 word pairs, then shows 
how long each method took to run.

## Why This Matters
A dictionary in Python is a hash table. Looking up any word takes the 
same amount of time whether there are 10 words or 100,000 words in it.

A list has to check every item one by one. On a book with 110,000 words 
this gets very slow very fast.

## How to Run
Download Adventures of Huckleberry Finn from Project Gutenberg and save 
it in the same folder as the script, then run:

```bash
python final_assingment_luis.py
```

## Files
- `final_assingment_luis.py` — the Python script
- Text file: download from https://www.gutenberg.org/ebooks/76

## Tools Used
- Python 3
- Standard library only — no installs needed

## Course
Algorithms and Data Structures — Seneca Polytechnic
Honours Bachelor of Data Science and Analytics, Semester 3
