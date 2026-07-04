# Week 03 Quiz — Hatchling Dash — Sprites & Motion — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 03: Hatchling Dash — Sprites & Motion.*

## Questions

1. Write Python Turtle code to set the turtle's position to (100, -50) without drawing.
2. What is the difference between absolute and relative movement in Scratch?
3. Which Python Turtle command stamps a copy of the turtle shape?
4. How would you make a sprite follow the mouse pointer in Scratch?
5. What are the coordinates of the centre of the Scratch stage?
6. Write code to make a turtle walk forward until it touches the edge of the screen.
7. What does the 'if on edge, bounce' block do?
8. Explain how costumes relate to animation frames.
9. Which CBE competency is strengthened when learners debug sprite motion?
10. Give the coordinate pairs for the four corners of a standard Scratch stage.

## Answer Key

1. import turtle; t = turtle.Turtle(); t.penup(); t.setpos(100, -50)
2. Absolute uses exact coordinates; relative uses change by/direction.
3. t.stamp()
4. Forever: point towards mouse-pointer, move 5 steps.
5. x=0, y=0.
6. while not t.xcor() > 300: t.forward(5)
7. It reverses direction when a sprite hits the stage edge.
8. Each costume is one frame; switching quickly creates animation.
9. Critical Thinking and Problem Solving.
10. Top-left (-240,180), top-right (240,180), bottom-right (240,-180), bottom-left (-240,-180).
