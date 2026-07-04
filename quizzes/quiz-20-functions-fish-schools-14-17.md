# Week 20 Quiz — Functions for Fish Schools — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 20: Functions for Fish Schools.*

## Questions

1. Write a Python function called draw_fish(size) that prints a simple fish shape.
2. What is the difference between a parameter and an argument?
3. What does return do in a function?
4. Write a function that returns the bigger of two numbers.
5. What is a side effect?
6. Explain why functions improve maintainability.
7. Write a function that calculates the area of a reef given width and length.
8. What is recursion?
9. Write a recursive function to count down from n to 1.
10. Map functions to a CBE Algorithms outcome.

## Answer Key

1. def draw_fish(size):
    print('<' + '-'*size + '><')
2. A parameter is in the definition; an argument is the value passed in.
3. It sends a value back to the caller.
4. def bigger(a, b):
    return a if a > b else b
5. Something a function does besides returning a value, like printing.
6. Changes only need to happen in one place.
7. def reef_area(w, l): return w * l
8. A function that calls itself.
9. def countdown(n):
    if n <= 0: return
    print(n); countdown(n-1)
10. Learners design reusable procedures to solve sub-problems.
