# Week 31 Quiz — Radio Tag — micro:bit Networks — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 31: Radio Tag — micro:bit Networks.*

## Questions

1. Write micro:bit code that receives a radio message and displays it.
2. What is a protocol and why is it needed in networking?
3. Explain broadcast vs point-to-point communication.
4. How would you add a checksum to a simple tag message?
5. What is packet loss and how might it affect shark tracking?
6. Write code to set a radio group so two micro:bits can talk privately.
7. What is latency in a radio network?
8. How would you store received tag IDs for later analysis?
9. Explain the difference between Bluetooth and micro:bit radio.
10. Map radio networks to a CBE Networks outcome.

## Answer Key

1. from microbit import *
import radio
radio.on()
while True:
    msg = radio.receive()
    if msg:
        display.scroll(msg)
2. A set of rules so devices understand each other.
3. Broadcast sends to all; point-to-point sends to one specific device.
4. Append a simple hash like sum of ASCII values mod 256.
5. Some messages are not received, causing gaps in the track.
6. radio.config(group=7); radio.on()
7. Delay between sending and receiving a message.
8. Append them to a list with timestamps.
9. Bluetooth pairs devices; micro:bit radio is simpler broadcast.
10. Learners use simple wireless communication to exchange data.
