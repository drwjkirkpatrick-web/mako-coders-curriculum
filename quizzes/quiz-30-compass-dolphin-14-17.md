# Week 30 Quiz — Compass Dolphin — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 30: Compass Dolphin.*

## Questions

1. Write micro:bit code that displays an arrow pointing north.
2. How does a digital compass detect direction?
3. What causes compass interference near electronics?
4. Write a function that returns the cardinal direction for a heading.
5. How would you log heading data during a dolphin tracking simulation?
6. What is dead reckoning and why is it hard without GPS?
7. Explain how sensor fusion could improve direction tracking.
8. Write code to smooth noisy compass readings.
9. What is bearing and how does it differ from heading?
10. Map compass/direction to CBE Computers and Data outcomes.

## Answer Key

1. from microbit import *
while True:
    display.show(Image.ALL_ARROWS[compass.heading() // 45])
2. It measures Earth's magnetic field with a magnetometer.
3. Metal and magnets can distort the magnetic field.
4. def cardinal(h):
    dirs = ['N','NE','E','SE','S','SW','W','NW']
    return dirs[int((h + 22.5) % 360 / 45)]
5. Store (time, heading) tuples in a list.
6. Estimating position from direction and distance; errors accumulate.
7. Combine compass with accelerometer for tilt compensation.
8. readings = [compass.heading() for _ in range(5)]; h = sum(readings)/5
9. Bearing is direction to a target; heading is direction you face.
10. Learners collect and interpret orientation data.
