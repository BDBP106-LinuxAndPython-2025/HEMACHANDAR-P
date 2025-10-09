#!/usr/bin/python3

# (11) Write a decorator log_function_call that prints Running DNA analysis.... before
# and Analysis complete! after any function. Apply it to the above function that returns
# the GC % of a DNA sequence.

#!/usr/bin/python3

# (11) Write a decorator log_function_call that prints messages before and after a function.

# Decorator definition
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Running DNA analysis....")
        result = func(*args, **kwargs)
        print("Analysis complete!")
        return result
    return wrapper

# Function to calculate GC content with decorator applied
@log_function_call
def gc_content(seq):
    seq = seq.upper()
    gc = seq.count('G') + seq.count('C')
    gc_percent = (gc / len(seq)) * 100
    print(f"GC content: {gc_percent:.2f}%")
    return gc_percent

# Main input
sequence = input("Enter sequence to analyse: ")
gc_content(sequence)
