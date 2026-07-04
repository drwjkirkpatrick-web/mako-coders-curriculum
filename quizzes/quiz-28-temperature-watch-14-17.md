# Week 28 Quiz — Temperature Watch — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 28: Temperature Watch.*

## Questions

1. Write a micro:bit program that records temperature every minute and alerts if it exceeds 30°C.
2. What is a moving average and why use it with sensor data?
3. How would you plot temperature readings over time?
4. Explain the difference between accuracy and precision.
5. Write code to compute the average of the last 5 readings.
6. What is an actuator? Give an example.
7. How would you send an alert without a screen?
8. Why does coral bleach when water is too warm?
9. Design a threshold with hysteresis: alert above 30, cancel below 27.
10. Map temperature monitoring to CBE outcomes.

## Answer Key

1. from microbit import *
readings = []
while True:
    t = temperature()
    readings.append(t)
    if t > 30:
        display.show(Image.SAD)
    sleep(60000)
2. Average of recent readings; it reduces noise.
3. Store (time, temp) pairs and plot temp vs time.
4. Accuracy is closeness to true value; precision is consistency of repeated readings.
5. avg = sum(readings[-5:]) / len(readings[-5:])
6. A device that acts on the world, e.g., a buzzer or LED.
7. Use a buzzer, radio, or flashing LED.
8. It loses the algae that give it colour and food.
9. if t > 30: alert = True; elif t < 27: alert = False
10. Computers (sensors), Data (logging), Citizenship (conservation).
