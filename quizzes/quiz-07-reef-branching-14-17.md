# Week 07 Quiz — Reef Branching — If-Else Ladders — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 07: Reef Branching — If-Else Ladders.*

## Questions

1. Write a Python function that returns the reef zone for a given depth.
2. When should you use if-elif-else instead of many independent ifs?
3. What is the bug in this ladder? if x > 5: ... elif x > 10: ...
4. Convert this to a dictionary lookup: if species == 'dolphin': return 2; elif species == 'shark': return 5; else: return 0.
5. Write a ladder that assigns protection level based on IUCN status.
6. What is fall-through and how do you prevent it in Python?
7. Explain how branching supports adaptive learning software.
8. Which Boolean expression is true only when depth is between 5 and 15?
9. How do you handle invalid user input in a branching program?
10. Map if-else ladders to a CBE learning outcome in the Algorithms strand.

## Answer Key

1. def reef_zone(depth):
    if depth < 5: return 'shallow'
    elif depth < 20: return 'fore-reef'
    else: return 'deep'
2. When only one branch should run.
3. The second condition will never run because the first catches all x > 5, including > 10.
4. { 'dolphin': 2, 'shark': 5 }.get(species, 0)
5. if status == 'CR': return 'urgent'; elif status == 'EN': return 'high'; elif status == 'VU': return 'medium'; else: return 'low'
6. Fall-through runs multiple branches; use elif to prevent it.
7. The program changes difficulty based on the learner's score.
8. depth >= 5 and depth <= 15
9. Add an else/default branch that asks again or shows an error.
10. Learners select appropriate control structures for multi-way decisions.
