# Week 17 Quiz — Filtering the Plankton — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 17: Filtering the Plankton.*

## Questions

1. Write a Python list comprehension that keeps only species longer than 3 metres.
2. What is the difference between filtering and sorting a list?
3. Write a function filter_endangered(species, status) that returns only endangered species.
4. How do you filter a dictionary by value?
5. What is the output of [x for x in [1,2,3,4] if x % 2 == 0]?
6. Explain why filtering is a form of abstraction.
7. Write code that filters a DataFrame for rows where country == 'Kenya'.
8. What is a predicate in filtering?
9. How would you test a filter function?
10. Map filtering to a CBE Data strand outcome.

## Answer Key

1. big = [s for s in species if lengths[s] > 3]
2. Filtering removes items; sorting reorders them.
3. def filter_endangered(species, status):
    return [s for s in species if status[s] == 'endangered']
4. Use a dict comprehension: {k:v for k,v in d.items() if v > threshold}
5. [2, 4]
6. It hides the items that do not match, leaving only what matters.
7. df[df['country'] == 'Kenya']
8. A function that returns True or False for each item.
9. Give it a small list with known matches and non-matches.
10. Learners extract relevant data using conditions.
