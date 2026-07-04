# Week 35 Quiz — Automate the Tide Log — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 35: Automate the Tide Log.*

## Questions

1. Write a Python script that appends the current time and tide height to a CSV file.
2. What is the difference between CSV and JSON file formats?
3. How would you schedule a Python script to run every hour on Linux?
4. Explain file handling context managers and why to use them.
5. Write code that reads a log and counts how many readings exceeded 2 metres.
6. What is log rotation?
7. How do you avoid data loss if a program crashes while writing a file?
8. What is a timestamp and why include it in logs?
9. How would you parse a CSV log into a list of dictionaries?
10. Map file automation to CBE Algorithms/Data outcomes.

## Answer Key

1. import datetime
with open('tides.csv','a') as f:
    f.write(f'{datetime.now().isoformat()},1.2\n')
2. CSV is rows of comma-separated values; JSON is structured key-value pairs.
3. Use cron: 0 * * * * python3 script.py
4. with open(...) automatically closes the file even if an error occurs.
5. with open('tides.txt') as f:
    count = sum(1 for line in f if float(line.strip()) > 2)
6. Archiving old log files so current logs stay small.
7. Write to a temporary file, then rename it.
8. It records exactly when each entry was created.
9. Use csv.DictReader.
10. Learners write programs that persist and process data over time.
