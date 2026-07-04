# Week 10 Quiz — Debug the Mangrove — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 10: Debug the Mangrove.*

## Questions

1. What is the difference between a syntax error and a runtime error?
2. What Python error appears when you use a variable before defining it?
3. How do you use print() for debugging?
4. What is a stack trace and why is it useful?
5. Write a try/except block that handles dividing by zero.
6. Explain rubber-duck debugging.
7. What is a breakpoint?
8. Why should tests be small and focused?
9. Which debugging strategy would you use if a loop gives unexpected values?
10. Which CBE competency is most developed by systematic debugging?

## Answer Key

1. Syntax error breaks language rules; runtime error occurs while running.
2. NameError
3. Add print() statements to show variable values at different points.
4. It shows the sequence of function calls that led to an error.
5. try:
    x = 10 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')
6. Explaining your code out loud to an object helps you spot mistakes.
7. A marker that pauses execution at a specific line so you can inspect state.
8. They isolate bugs and prove one thing at a time.
9. Print the loop counter each iteration.
10. Critical Thinking and Problem Solving.
