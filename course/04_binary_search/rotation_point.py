def binary_search(words, target):
    floor = -1
    ceiling = len(words)

    while floor+1 < ceiling:
        distance = ceiling - floor
        guess = floor + (distance // 2)
        # For fun, to see how long it takes
        # If we're right
        print(f"Looking at index {guess}")
        if words[guess] == target:
            return words[guess]
        # If we're past the target
        elif words[guess] > target:
            # Target is to our left, so only look there
            floor = guess
        else: # The target is to our right
            ceiling = guess # So we ignore everything to our right
    # If we reached this point, target is not in the dictionary.
    return False

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

# You can use arithmetic comparison operators for strings in Python so this
# code will be much more legible than it would be in some other languages.
# For further legibility, we will just search for the word we know is at the
# rotation point instead of trying to define it programmatically and match an
# expression.
print(binary_search(words, 'asymptote'))
