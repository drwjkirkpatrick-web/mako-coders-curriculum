# Week 27 Quiz — Inputs from the Ocean — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 27: Inputs from the Ocean.*

## Questions

1. Write micro:bit code that reads button A and sends 'splash' to the serial port.
2. What is the difference between polling and interrupt-driven input?
3. Explain analog-to-digital conversion in simple terms.
4. How would you debounce a mechanical button in code?
5. Write a function read_button() that returns 'A', 'B', or 'none'.
6. What is a pull-up resistor used for?
7. How would you log button presses with timestamps?
8. Name two real sensors used in ocean monitoring.
9. What is sensor calibration?
10. Map inputs to a CBE Computers outcome.

## Answer Key

1. from microbit import *
while True:
    if button_a.was_pressed():
        print('splash')
    sleep(100)
2. Polling repeatedly checks; interrupts react immediately to an event.
3. It turns a continuous measurement like temperature into a digital number.
4. Wait a short time after detecting a press before checking again.
5. def read_button():
    if button_a.is_pressed(): return 'A'
    if button_b.is_pressed(): return 'B'
    return 'none'
6. It keeps an input at a known high state until a button connects it to ground.
7. Store (time, button) tuples in a list.
8. Temperature sensor, salinity sensor, pH sensor, turbidity sensor.
9. Adjusting readings so they match known real values.
10. Learners read data from hardware sensors.
