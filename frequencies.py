"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):


    frequencies = {}
    # iterating over the list
    output = [str(x) for x in items]
    for i in output:
   # checking the element in dictionary
        if i in frequencies:
      # incrementing the counr
            frequencies[i] += 1
        else:
      # initializing the count
            frequencies[i] = 1

    return frequencies
