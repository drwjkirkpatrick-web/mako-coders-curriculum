# Week 19 Quiz — Dictionary of the Dugong — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 19: Dictionary of the Dugong.*

## Questions

1. Write a Python dictionary that maps three Kenyan species to their IUCN status.
2. What is a key-value pair?
3. How is a dictionary implemented in Python?
4. Write code that safely reads a value, defaulting to 'unknown' if the key is missing.
5. How do you loop over both keys and values?
6. What makes a dictionary key valid?
7. Write a dictionary comprehension that counts letters in a word.
8. Explain when to use a dict instead of a list.
9. How would you merge two dictionaries?
10. Map dictionaries to a CBE Data strand outcome.

## Answer Key

1. status = {'mako': 'VU', 'green_turtle': 'EN', 'whale_shark': 'EN'}
2. A key that identifies an item and a value that stores its data.
3. As a hash table for fast key lookup.
4. status.get('dugong', 'unknown')
5. for species, st in status.items(): ...
6. It must be hashable, like a string, number, or tuple.
7. {letter: word.count(letter) for letter in set(word)}
8. Use a dict for labelled lookup; use a list for ordered sequences.
9. Use update() or {**a, **b}.
10. Learners store and retrieve structured data using labelled keys.
