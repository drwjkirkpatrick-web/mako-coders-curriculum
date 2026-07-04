# Week 29 Quiz — Tide-guard Light — Ages 10–13

> *10 code-focused, CBE-aligned questions for Week 29: Tide-guard Light.*

## Questions

1. What is an output on a micro:bit?
2. Which block lights an LED on the micro:bit display?
3. How do you turn all LEDs on?
4. Write code to flash the centre LED three times.
5. What colour is a micro:bit LED display?
6. Why use a light as a tide warning?
7. What does brightness 0 mean?
8. What does brightness 9 mean?
9. How do you clear the display?
10. Which CBE strand links to outputs?

## Answer Key

1. Something the micro:bit controls, like an LED.
2. display.set_pixel(x, y, 9)
3. display.show(Image.HEART)
4. for _ in range(3):
    display.set_pixel(2,2,9); sleep(200); display.set_pixel(2,2,0); sleep(200)
5. Red.
6. People can see it from far away.
7. Off.
8. Maximum brightness.
9. display.clear()
10. Computers.
