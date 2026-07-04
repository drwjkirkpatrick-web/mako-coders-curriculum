# Week 44 Quiz — Events and the Game Loop — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 44: Events and the Game Loop.*

## Questions

1. Write the skeleton of a Pygame Zero game with update() and draw() functions.
2. What is the difference between update() and draw() in a game loop?
3. How do you keep movement frame-rate independent?
4. Explain collision detection in a 2D game.
5. Write code to clamp a value between a minimum and maximum.
6. What is a state machine and how does it help game design?
7. How would you handle multiple key presses at once?
8. What is double buffering and why is it used?
9. Write code to detect when a shark leaves the screen.
10. Map game loops to CBE Algorithms outcomes.

## Answer Key

1. import pgzrun
def update(): pass
def draw(): screen.fill('black')
pgzrun.go()
2. update() changes state; draw() renders the current state.
3. Multiply speed by delta time.
4. Check if the bounding boxes or circles of two objects overlap.
5. x = max(min_x, min(x, max_x))
6. A model with distinct states like 'menu', 'playing', 'game over'.
7. Track key states in a dictionary or use built-in keyboard properties.
8. Drawing to an off-screen buffer to prevent flickering.
9. if shark.x < 0 or shark.x > WIDTH: shark.x = WIDTH/2
10. Learners implement real-time interactive programs.
