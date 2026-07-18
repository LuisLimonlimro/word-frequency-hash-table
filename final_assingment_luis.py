"""
Word Frequency Counter Using Hash Tables
Author: Luis Limon
Student Number: 163600174
Description: Reads Adventures of Huckleberry Finn, preprocesses text (lowercase, remove punctuation),
splits into words, counts frequencies using Python dictionary (hash table) with O(1) lookups,
and displays top 20 most frequent words and top 10 word pairs in table format.
"""

import re          # Regular expressions library — not used directly but imported for text pattern matching
import string      # Gives us access to string.punctuation — a string of all punctuation characters
import os          # Operating system tools — not used directly but available for file path operations
import time        # Used to measure how long each counting method takes to run

class TextProcessor:
    # Class that handles all steps: reading, cleaning, counting, and displaying results

    def __init__(self, filename):
        # Constructor — runs automatically when you create a TextProcessor object
        self.filename = filename       # Store the name of the text file to read later
        self.text = None               # Will hold the raw text after reading the file
        self.words = None              # Will hold the list of cleaned individual words
        self.word_counts = None        # Will hold the dictionary of word → count pairs
        self.bigram_counts = None      # Will hold the dictionary of word pair → count pairs

    def read_file(self):
        # Tries to open the file using different text encodings
        # Old books from Project Gutenberg often use latin-1 instead of utf-8
        encodings = ['latin-1', 'utf-8', 'cp1252']  # List of encodings to try in order

        for encoding in encodings:
            # Try each encoding one at a time
            try:
                with open(self.filename, 'r', encoding=encoding) as file:
                    # Open file in read mode using current encoding
                    self.text = file.read()               # Read entire file content into self.text
                print(f"Loaded with {encoding}")          # Tell user which encoding worked
                return self.text                          # Return the raw text and stop trying
            except UnicodeDecodeError:
                # If this encoding fails, move on to the next one
                continue

        # If all three encodings fail, raise an error with a clear message
        raise ValueError("All encodings failed")

    def clean_text(self):
        # Converts raw text into a clean list of lowercase words with no punctuation
        if not self.text:
            # Safety check — make sure read_file() was called first
            raise ValueError("Run read_file() first!")

        text_lower = self.text.lower()   # Convert all characters to lowercase so "The" and "the" match

        translator = str.maketrans('', '', string.punctuation)
        # str.maketrans creates a translation table that maps every punctuation character to nothing
        # string.punctuation contains: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

        clean_text = text_lower.translate(translator)   # Apply the translation table — removes all punctuation

        self.words = clean_text.split()  # Split the cleaned string into a list of individual words on whitespace
        return self.words                # Return the word list

    def count_words(self):
        # Counts word frequencies using a Python dictionary (hash table) — O(1) per lookup
        if not self.words:
            # Safety check — make sure clean_text() was called first
            raise ValueError("Run clean_text() first!")

        # --- Count single words ---
        self.word_counts = {}            # Start with an empty dictionary (this is the hash table)

        for word in self.words:
            # Loop through every word in the cleaned word list
            self.word_counts[word] = self.word_counts.get(word, 0) + 1
            # .get(word, 0) returns current count for this word, or 0 if it hasn't been seen yet
            # Then adds 1 to that count and stores it back in the dictionary

        # --- Count word pairs (bigrams) ---
        self.bigram_counts = {}          # Start with an empty dictionary for pairs

        for i in range(len(self.words) - 1):
            # Loop through all words except the last one (since we need the word after each one)
            bigram = (self.words[i], self.words[i+1])
            # Create a tuple of two consecutive words e.g. ("tom", "sawyer")
            self.bigram_counts[bigram] = self.bigram_counts.get(bigram, 0) + 1
            # Same counting logic as single words — increment count for this pair

    def count_words_list(self):
        # Counts word frequencies using a list instead of a dictionary
        # This is intentionally slow — used to demonstrate why hash tables are better
        if not self.words:
            raise ValueError("Run clean_text() first!")

        word_list = []                   # Start with an empty list to store (word, count) tuples

        for word in self.words:
            # Loop through every word
            found = False                # Flag to track whether we found this word in the list

            for i in range(len(word_list)):
                # Scan the entire list from the beginning every time — this is O(n) per word
                if word_list[i][0] == word:
                    # If this word already exists in the list
                    word_list[i] = (word, word_list[i][1] + 1)
                    # Replace the tuple with an updated count
                    found = True         # Mark as found so we don't add a duplicate
                    break                # Stop scanning — no need to check the rest of the list

            if not found:
                word_list.append((word, 1))
                # Word not in list yet — add it with count of 1

        self.word_counts = dict(word_list)   # Convert the list of tuples back to a dictionary

    def get_top_words(self, n=20):
        # Sorts all words by count (highest first) and prints the top n in a formatted table
        if not self.word_counts:
            raise ValueError("Run count_words() first!")

        sorted_items = sorted(self.word_counts.items(), key=lambda x: x[1], reverse=True)
        # .items() returns all (word, count) pairs
        # sorted() sorts them by count (x[1]) in descending order (reverse=True)

        top_n = sorted_items[:n]         # Take only the first n items from the sorted list

        # Print formatted table header
        print("\n" + "=" * 40)
        print(f"TOP {n} WORDS")
        print("=" * 40)
        print(f"{'Word':<15} {'Count':>8}")   # Left-align word in 15 chars, right-align count in 8 chars
        print("-" * 40)

        for word, count in top_n:
            # Loop through top n words and print each row
            print(f"{word:<15} {count:>8}")   # Same alignment as header

        print("=" * 40 + "\n")               # Bottom border

    def get_top_bigrams(self, n=10):
        # Sorts all word pairs by count (highest first) and prints the top n in a formatted table
        if not self.bigram_counts:
            raise ValueError("Run count_words() first!")

        sorted_bigrams = sorted(self.bigram_counts.items(), key=lambda x: x[1], reverse=True)
        # Same sorting logic as get_top_words — sort pairs by count descending

        top_n = sorted_bigrams[:n]       # Take only the first n pairs

        # Print formatted table header
        print("\n" + "=" * 50)
        print(f"TOP {n} WORD PAIRS")
        print("=" * 50)
        print(f"{'Pair':<20} {'Count':>8}")
        print("-" * 50)

        for (word1, word2), count in top_n:
            # Unpack each bigram tuple into word1 and word2
            print(f"{word1} {word2:<12} {count:>8}")   # Print pair side by side with count

        print("=" * 50 + "\n")           # Bottom border


# ── MAIN PROGRAM ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # This block only runs when the script is executed directly (not imported)

    processor = TextProcessor('adventures_of_huckleberry_finn.txt')
    # Create a TextProcessor object pointing to the book file

    processor.read_file()    # Step 1: Read the raw text from the file
    processor.clean_text()   # Step 2: Lowercase and remove punctuation

    # ── Time the hash table method ──
    start_hash = time.time()     # Record start time before hash counting
    processor.count_words()      # Run the fast dictionary-based word counter
    hash_time = time.time() - start_hash   # Calculate elapsed time

    # Save bigrams before the list method overwrites word_counts
    bigram_copy = processor.bigram_counts.copy()   # Keep a backup of bigram results
    processor.word_counts = None                    # Clear word_counts so list method starts fresh

    # ── Time the list method ──
    start_list = time.time()         # Record start time before list counting
    processor.count_words_list()     # Run the slow list-based word counter
    list_time = time.time() - start_list   # Calculate elapsed time

    # ── Display results ──
    processor.get_top_words(20)      # Print top 20 most frequent words
    processor.get_top_bigrams(10)    # Print top 10 most frequent word pairs

    # ── Print performance comparison ──
    print(f"Hash: {hash_time:.3f}s vs List: {list_time:.3f}s")
    # Shows how much faster the hash table was compared to the list

    print(f"   Total words: {len(processor.words):,}")
    # Total number of words in the book (with commas for readability)

    print(f"   Unique words: {len(processor.word_counts):,}")
    # Number of distinct words found in the book

    print(f"   'the': {processor.word_counts.get('the', 0)}")
    # How many times the word "the" appears — expected to be the most common word
