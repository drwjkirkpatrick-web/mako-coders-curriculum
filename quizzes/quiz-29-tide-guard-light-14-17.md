# Week 29 Quiz — Tide-guard Light — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 29: Tide-guard Light.*

## Questions

1. Write micro:bit code that pulses an LED pattern when high tide is predicted.
2. How do PWM and LED brightness relate?
3. What is the difference between a digital and analog output?
4. Write code to control an external LED on pin 0.
5. How would you drive a small motor from a micro:bit?
6. Explain why you need a transistor or relay for high-power outputs.
7. What safety concern applies to tide-warning lights near water?
8. Write a function that maps tide height to LED brightness.
9. How would you add sound to a tide warning?
10. Map outputs to a CBE Computers outcome.

## Answer Key

1. from microbit import *
def tide_warning():
    for b in range(10):
        display.set_pixel(2,2,b)
        sleep(50)
    display.clear()
2. PWM varies on-time to control average brightness.
3. Digital is on/off; analog can vary in level.
4. pin0.write_digital(1)
5. Use a motor driver board because the micro:bit cannot supply enough current.
6. Microcontrollers provide low current; transistors/relays switch higher loads.
7. Waterproofing and electrical isolation.
8. def brightness(height): return min(9, int(height * 2))
9. Attach a buzzer and use pin0.write_analog(frequency).
10. Learners control hardware actuators based on program logic.
