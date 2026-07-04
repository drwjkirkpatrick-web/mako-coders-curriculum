# Week 22 Quiz — Survey Data — 2023 Aerial Count — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 22: Survey Data — 2023 Aerial Count.*

## Questions

1. How would you store 2023 aerial survey data in Python?
2. Write Python code to read a CSV file using the standard library.
3. What is the difference between a sample and a population in a survey?
4. How do you calculate the average sightings per day from a list?
5. Write code to find the day with the most sightings.
6. What is a pandas DataFrame and why is it useful?
7. Explain why data cleaning is important.
8. Write code to filter survey rows where species == 'whale_shark'.
9. What is metadata? Give an example.
10. Map survey data to a CBE Data outcome.

## Answer Key

1. As a CSV file or a list of dictionaries.
2. import csv; rows = list(csv.reader(open('survey.csv')))
3. A population is all items; a sample is a subset.
4. sum(sightings) / len(sightings)
5. max(sightings)
6. A 2D table structure with labels; good for analysis.
7. Errors or missing values can make analysis wrong.
8. df[df['species'] == 'whale_shark']
9. Data about data, e.g., date, location, observer name.
10. Learners collect, clean, and summarise real-world data sets.
