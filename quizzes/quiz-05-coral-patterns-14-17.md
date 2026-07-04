# Week 05 Quiz — Coral Patterns — Nested Loops — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 05: Coral Patterns — Nested Loops.*

## Questions

1. Write Python code for a nested loop that prints a 3x3 grid of asterisks.
2. What is the time complexity of a simple nested loop where each loop runs n times?
3. How would you use nested loops to draw a checkerboard of coral and sand?
4. Write code that draws 5 concentric circles using nested loops.
5. What is the output of this nested loop? for i in range(2): for j in range(2): print(i,j)
6. Explain the difference between nested loops and a single loop that repeats twice as long.
7. In a tile map, which loop index usually represents x and which y?
8. Write a nested loop that counts how many coral tiles are in a 4x4 reef if each tile has 70% coral coverage.
9. Why must the inner loop reset its counter each time the outer loop runs?
10. Map nested loops to a CBE learning outcome for Algorithms.

## Answer Key

1. for row in range(3):
    for col in range(3):
        print('*', end=' ')
    print()
2. O(n²).
3. Outer loop rows; inner loop columns; use (row+col) % 2 to pick colour.
4. Use an outer loop to change radius and an inner loop to draw each circle.
5. 0 0, 0 1, 1 0, 1 1.
6. Nested loops combine two independent counts; a single loop has only one counter.
7. Inner loop = x/columns; outer loop = y/rows.
8. Use nested loops to count 16 tiles, then multiply by 0.7 (round to 11).
9. Otherwise it would not start a new row/column correctly.
10. Learners apply repetition structures to model 2D patterns.
