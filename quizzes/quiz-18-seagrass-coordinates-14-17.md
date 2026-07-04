# Week 18 Quiz — Seagrass Coordinates — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 18: Seagrass Coordinates.*

## Questions

1. Write Python code to plot a point at latitude -4.0 and longitude 39.5.
2. What is the difference between Cartesian and geographic coordinates?
3. How would you store many coordinate points in Python?
4. Write a loop that draws a dot at each coordinate in a list.
5. What is a bounding box?
6. How do you check if a point is inside a rectangle?
7. Explain how coordinates relate to arrays in image processing.
8. Write a function distance(x1, y1, x2, y2) using the Pythagorean theorem.
9. What projection challenge occurs when mapping a sphere to a flat screen?
10. Map coordinate systems to a CBE Data/Algorithms outcome.

## Answer Key

1. import matplotlib.pyplot as plt; plt.scatter(39.5, -4.0)
2. Cartesian uses x/y; geographic uses latitude/longitude.
3. As a list of tuples: points = [(39.5, -4.0), (40.1, -3.8)]
4. for x, y in points:
    plt.scatter(x, y)
5. The rectangle defined by minimum and maximum coordinates.
6. Check x between left/right and y between bottom/top.
7. Each pixel has an (x,y) position and a colour value.
8. import math; return math.sqrt((x2-x1)**2 + (y2-y1)**2)
9. Distortion of size/shape near the poles.
10. Learners represent and use positional data in computational models.
