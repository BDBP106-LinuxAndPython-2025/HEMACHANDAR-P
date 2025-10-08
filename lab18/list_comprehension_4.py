#!/usr/bin/pyhton3

from collections import Counter

sentence = "She sells sea shells that she collects from the sea floor"
words = [word.lower() for word in sentence.split()]  # normalize to lowercase

counts = Counter(words)

# List of words appearing more than once
repeated_words = [word for word, count in counts.items() if count > 1]

print(repeated_words)
# Output: ['she', 'sea']
