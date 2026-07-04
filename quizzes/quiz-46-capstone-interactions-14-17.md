# Week 46 Quiz — Capstone Build 2 — Interactions — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 46: Capstone Build 2 — Interactions.*

## Questions

1. Write a collision function that checks overlap of two rectangles.
2. What is the difference between AABB and circle collision detection?
3. How would you implement a scoring system with combos?
4. Write code to spawn a new fish after one is collected.
5. What is a hitbox?
6. How do you prevent the same interaction from triggering twice in one frame?
7. Explain event-driven vs polling input in Pygame Zero.
8. What is game feel and how do interactions create it?
9. How would you log interaction events for later analysis?
10. Map game interactions to CBE Algorithms/Creativity outcomes.

## Answer Key

1. def collide(a, b):
    return a.x < b.x + b.w and a.x + a.w > b.x and a.y < b.y + b.h and a.y + a.h > b.y
2. AABB uses rectangles; circle uses distance from centres.
3. Increase multiplier when multiple quick interactions happen.
4. import random; fish.x = random.randint(50, WIDTH-50); fish.y = random.randint(50, HEIGHT-50)
5. The invisible shape used for collision checks.
6. Use a flag or cooldown timer.
7. Event-driven reacts to key events; polling checks keyboard state each frame.
8. The satisfying response to player actions, e.g., juice, screenshake.
9. Append events to a list with timestamps.
10. Learners design responsive, engaging systems.
