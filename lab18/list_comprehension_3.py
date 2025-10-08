#!/usr/bin/python3

sentence = "She sells sea shells that she collects from the sea floor"
words = sentence.split()

# Find the length of the longest word
max_length = max(len(word) for word in words)

# Get the longest word(s)
longest_words = [word for word in words if len(word) == max_length]

# Print the first longest word
print(longest_words[0])
# Output: collects
