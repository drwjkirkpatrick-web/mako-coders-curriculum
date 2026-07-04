# Week 32 Quiz — Simulated Shark Tracker — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 32: Simulated Shark Tracker.*

## Questions

1. Write Python code that simulates a shark moving randomly in 2D for 50 steps.
2. What is a random walk and why is it a simple movement model?
3. How would you add boundaries to a simulation?
4. Write code to plot a simulated shark path.
5. What is a seed in a random number generator?
6. How do you simulate sensor noise?
7. Explain Monte Carlo methods in one sentence.
8. Write a function that returns distance from shore given x, y coordinates.
9. How would you validate a simulation against real data?
10. Map simulations to CBE Algorithms/Data outcomes.

## Answer Key

1. import random
x, y = 0, 0
for _ in range(50):
    x += random.choice([-1,1])
    y += random.choice([-1,1])
2. Each step is random; it approximates movement with no preferred direction.
3. Check if x or y exceeds limits and bounce or clamp.
4. import matplotlib.pyplot as plt; plt.plot(xs, ys); plt.show()
5. A starting value that makes randomness reproducible.
6. Add a small random value to each reading.
7. Using repeated random sampling to estimate results.
8. import math; return math.sqrt(x**2 + y**2)
9. Compare statistics like average speed and range.
10. Learners model real-world systems using computational methods.
