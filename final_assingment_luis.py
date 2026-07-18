



"""
Word Frequency Counter Using Hash Tables
Author: Luis Limon
Student Number: 163600174
Description: Reads Adventures of Huckleberry Finn, preprocesses text (lowercase, remove punctuation),
splits into words, counts frequencies using Python dictionary (hash table) with O(1) lookups,
and displays top 20 most frequent words in table format.
"""




import re
import string  
import os
import time
import string  # Punctuation removal
import time    # Speed testing

class TextProcessor:
    def __init__(self, filename):  # Constructor - input text file name
        self.filename = filename    # Store filename for later use
        self.text = None            # Empty placeholder for raw text
        self.words = None           # Empty placeholder for cleaned words
        self.word_counts = None     # Empty placeholder for word counts
        self.bigram_counts = None   # Empty placeholder for word pairs
    
    def read_file(self):
        encodings = ['latin-1', 'utf-8', 'cp1252']  # 3 common text encodings
        for encoding in encodings:
            try:
                with open(self.filename, 'r', encoding=encoding) as file:
                    self.text = file.read()
                print(f"Loaded with {encoding}")
                return self.text
            except UnicodeDecodeError:
                continue
        raise ValueError("All encodings failed")
    
    def clean_text(self):
        if not self.text:
            raise ValueError("Run read_file() first!")
        text_lower = self.text.lower()  # Convert to lowercase
        translator = str.maketrans('', '', string.punctuation)
        clean_text = text_lower.translate(translator)  # Remove punctuation
        self.words = clean_text.split()  # Split into words
        return self.words
    
    def count_words(self):  
        if not self.words:
            raise ValueError("Run clean_text() first!")
        
        # Count single words
        self.word_counts = {}  # Empty dictionary (hash table)
        for word in self.words:
            self.word_counts[word] = self.word_counts.get(word, 0) + 1
        
        # Count word pairs (BONUS!)
        self.bigram_counts = {}  # Empty dictionary for pairs
        for i in range(len(self.words) - 1):  # Loop to second-to-last word
            bigram = (self.words[i], self.words[i+1])  # Tuple of consecutive words
            self.bigram_counts[bigram] = self.bigram_counts.get(bigram, 0) + 1
    
    def count_words_list(self):  # Slow demo to prove hash tables win
        if not self.words:
            raise ValueError("Run clean_text() first!")
        word_list = []  # Empty list to store words
        for word in self.words:
            found = False
            for i in range(len(word_list)):
                if word_list[i][0] == word:
                    word_list[i] = (word, word_list[i][1] + 1)
                    found = True
                    break
            if not found:
                word_list.append((word, 1))
        self.word_counts = dict(word_list)  # Convert back to dictionary
    
    def get_top_words(self, n=20):
        if not self.word_counts:
            raise ValueError("Run count_words() first!")
        sorted_items = sorted(self.word_counts.items(), key=lambda x: x[1], reverse=True)
        top_n = sorted_items[:n]
        print("\n" + "=" * 40)
        print(f"TOP {n} WORDS")
        print("=" * 40)
        print(f"{'Word':<15} {'Count':>8}")
        print("-" * 40)
        for word, count in top_n:
            print(f"{word:<15} {count:>8}")
        print("=" * 40 + "\n")
    
    def get_top_bigrams(self, n=10):
        if not self.bigram_counts:
            raise ValueError("Run count_words() first!")
        sorted_bigrams = sorted(self.bigram_counts.items(), key=lambda x: x[1], reverse=True)
        top_n = sorted_bigrams[:n]
        print("\n" + "=" * 50)
        print(f"TOP {n} WORD PAIRS")
        print("=" * 50)
        print(f"{'Pair':<20} {'Count':>8}")
        print("-" * 50)
        for (word1, word2), count in top_n:
            print(f"{word1} {word2:<12} {count:>8}")
        print("=" * 50 + "\n")


if __name__ == "__main__":
    processor = TextProcessor('adventures_of_huckleberry_finn.txt')
    processor.read_file()
    processor.clean_text()
    
    # Hash timing
    start_hash = time.time()
    processor.count_words()  
    hash_time = time.time() - start_hash
    
    # Save bigrams before slow test overwrites
    bigram_copy = processor.bigram_counts.copy()
    processor.word_counts = None  
    
    start_list = time.time()
    processor.count_words_list()  
    list_time = time.time() - start_list
    
    processor.get_top_words(20)
    processor.get_top_bigrams(10)  # now works!!!
    
    print(f"Hash: {hash_time:.3f}s vs List: {list_time:.3f}s")
    print(f"   Total words: {len(processor.words):,}")
    print(f"   Unique words: {len(processor.word_counts):,}")
    print(f"   'the': {processor.word_counts.get('the', 0)}")
