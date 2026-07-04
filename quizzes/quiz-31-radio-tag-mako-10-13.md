# Week 31 Quiz — Radio Tag — micro:bit Networks — Ages 10–13

> *10 code-focused, CBE-aligned questions for Week 31: Radio Tag — micro:bit Networks.*

## Questions

1. What does the micro:bit radio do?
2. Which block turns the radio on?
3. Which block sends a message?
4. Write code to send a tag ID when button A is pressed.
5. What is a network?
6. Why would scientists use radio tags on sharks?
7. What could go wrong with a radio message?
8. How do two micro:bits know they are on the same network?
9. What is the range of a micro:bit radio?
10. Which CBE strand links to radio?

## Answer Key

1. It sends and receives messages between micro:bits.
2. radio.on()
3. radio.send('hello')
4. from microbit import *
import radio
radio.on()
while True:
    if button_a.is_pressed():
        radio.send('mako-01')
5. Connected devices that can communicate.
6. To track movement without following the animal.
7. It might not be received, or it could be lost.
8. They use the same channel/group.
9. Around 10–20 metres, depending on conditions.
10. Networks.
