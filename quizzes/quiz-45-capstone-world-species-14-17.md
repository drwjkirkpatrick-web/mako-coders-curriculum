# Week 45 Quiz — Capstone Build 1 — World & Species — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 45: Capstone Build 1 — World & Species.*

## Questions

1. Write a function load_species() that returns a list of species dictionaries.
2. How do you manage game assets without external images?
3. What is a world file or level file?
4. Write code to draw a species at a position from a dictionary.
5. How would you load species data from a JSON file?
6. What is the advantage of separating data from code?
7. Explain how to handle different screen sizes in a game.
8. How do you verify that all species appear in the world?
9. What is a configuration file and why use one?
10. Map capstone world-building to CBE Project/Data outcomes.

## Answer Key

1. def load_species():
    return [{'name':'mako','speed':5}, {'name':'turtle','speed':2}]
2. Use shapes, colours, text, and emoji-style drawings.
3. Data that describes the layout and contents of a game world.
4. s = species[0]; screen.draw.filled_circle((s['x'], s['y']), s['size'], s['colour'])
5. import json; data = json.load(open('species.json'))
6. You can change species without changing the program logic.
7. Use relative positions or scale based on WIDTH/HEIGHT.
8. Add temporary labels or print their positions.
9. A file that sets options without changing code, e.g., difficulty.
10. Learners build a structured, data-backed digital environment.
