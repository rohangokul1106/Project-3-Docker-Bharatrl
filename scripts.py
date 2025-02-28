import os
import re
import socket
from collections import Counter

# File paths
file1 = "/home/data/IF-1.txt"
file2 = "/home/data/AlwaysRememberUsThisWay-1.txt"
output_file = "/home/data/output/result.txt"

# Function to count words
def count_words(text):
    words = re.findall(r"\b\w+\b", text.lower())  # Split into words and count them
    return len(words), Counter(words)

# Handle contractions
def expand_contractions(text):
    contractions = {"i'm": "i am", "can't": "cannot", "don't": "do not"}
    for key, value in contractions.items():
        text = text.replace(key, value)
    return text

# Read and process files
with open(file1, "r", encoding="utf-8") as f:
    text1 = f.read()
word_count1, freq_words1 = count_words(text1)

with open(file2, "r", encoding="utf-8") as f:
    text2 = expand_contractions(f.read())  # Handle contractions before processing
word_count2, freq_words2 = count_words(text2)

# Get IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Get top 3 words
top_words1 = freq_words1.most_common(3)
top_words2 = freq_words2.most_common(3)

# Create the result content
results = f"""
Word count in IF-1.txt: {word_count1}
Word count in AlwaysRememberUsThisWay-1.txt: {word_count2}
Total word count: {word_count1 + word_count2}
Top 3 words in IF-1.txt: {top_words1}
Top 3 words in AlwaysRememberUsThisWay-1.txt (after handling contractions): {top_words2}
Container IP Address: {ip_address}
"""

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Write results to output file
print(f"Writing results to: {output_file}")
with open(output_file, "w") as f:
    f.write(results)

print("Results written successfully.")

