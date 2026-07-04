# Week 09 Quiz — Pod Click — Events — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 09: Pod Click — Events.*

## Questions

1. Write Python code that prints 'splash' when the user presses Enter.
2. What is an event-driven program?
3. In Pygame Zero, what function runs when the mouse is clicked?
4. Explain the difference between polling and event handling.
5. Write a micro:bit handler that shows a fish when button A is pressed.
6. What is a callback function?
7. How would you handle both a key press and a mouse click in one program?
8. Give an example of broadcast usage in a multi-sprite ocean scene.
9. What problem can occur if two events modify the same variable at the same time?
10. Which CBE competency is strengthened by designing interactive user controls?

## Answer Key

1. Use input('Press Enter to continue...'); print('splash')
2. A program that waits for events like clicks or messages and then reacts.
3. def on_mouse_down(): ...
4. Polling repeatedly checks a state; event handling reacts only when something happens.
5. from microbit import *
def on_button_a(): display.show(Image.FISH)
6. A function that runs automatically when an event occurs.
7. Register separate event handlers for each.
8. When dolphin is clicked, broadcast 'splash' so all fish swim away.
9. A race condition can cause incorrect values.
10. Digital Literacy and Creativity.
