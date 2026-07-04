# Week 21 Quiz — Turtle Nesting Timer — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 21: Turtle Nesting Timer.*

## Questions

1. Write Python code to wait for 2 seconds.
2. How do you record the current time in Python?
3. Write code that prints how long a block of code took to run.
4. What is epoch time?
5. How would you format a timestamp into a readable date?
6. Explain why timestamps are important in data logging.
7. Write a function that returns True if a turtle nesting took longer than 2 hours.
8. What is the difference between time.sleep() and a busy-wait loop?
9. How would you schedule a script to run every hour?
10. Map timers and timestamps to a CBE Data outcome.

## Answer Key

1. import time; time.sleep(2)
2. import time; start = time.time()
3. start = time.time(); ...; print(time.time() - start)
4. Seconds since 1 January 1970.
5. import datetime; datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
6. They show exactly when each measurement was taken.
7. def long_nest(seconds): return seconds > 7200
8. sleep() pauses efficiently; busy-waste wastes CPU.
9. Use a loop with time.sleep(3600) or a scheduler like cron.
10. Learners record and use time-based data.
