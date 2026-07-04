# Week 41 Quiz — Functions Revisited — Hunt Mode — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 41: Functions Revisited — Hunt Mode.*

## Questions

1. Write a Python function hunt_mode(is_day, energy) that returns True only during the day with enough energy.
2. What is a pure function?
3. Explain the difference between positional and keyword arguments.
4. Write a function with default parameters.
5. What is function composition?
6. How do you test a function with many possible inputs?
7. Write a recursive function for the Fibonacci sequence.
8. What is memoization and why use it?
9. How do docstrings help maintain functions?
10. Map advanced functions to CBE Algorithms outcomes.

## Answer Key

1. def hunt_mode(is_day, energy):
    return is_day and energy > 50
2. A function with no side effects and the same output for the same input.
3. Positional rely on order; keyword are named.
4. def greet(name, greeting='Hello'):
    print(greeting, name)
5. Using the output of one function as the input of another.
6. Use a table of test cases or small unit tests.
7. def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
8. Storing results of expensive function calls to avoid recomputation.
9. They describe what the function does, its parameters, and return value.
10. Learners design robust, reusable procedures for complex programs.
