"""
Word Occurrences
Estimate:  minutes
Actual:   apx 40 minutes
"""

text = input("Text: ").lower()

word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1

max_width = max(len(word) for word in word_counts)

for word, count in sorted(word_counts.items()):
    print(f"{word:>{max_width}} : {count}")
