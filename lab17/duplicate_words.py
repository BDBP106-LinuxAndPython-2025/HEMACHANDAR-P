#!usr/bin/pyhton3

#(5) Remove all duplicate words from a given sentence using a dictionary. (Hint: Use the
#set() function might be useful here.)

def remove_duplicates(sentence):
    words = sentence.split()
    a=set(words)
    print(a)
sentence = "this is is a test test sentence sentence"


 














    # seen = {}  # dictionary to track seen words preserving order
    #for word in words:
    #    if word not in seen:
    #        seen[word] = True  # mark the word as seen
    # Join all unique words back into a sentence
    #result = ' '.join(seen.keys())
    #return result
# Example usage:

#print(remove_duplicates(sentence))
