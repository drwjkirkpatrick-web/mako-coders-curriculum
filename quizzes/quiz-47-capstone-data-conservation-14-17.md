# Week 47 Quiz — Capstone Build 3 — Data & Conservation — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 47: Capstone Build 3 — Data & Conservation.*

## Questions

1. Write code that loads a JSON file of conservation facts and displays one randomly.
2. How would you integrate real survey data into a game without exposing sensitive locations?
3. What is a call-to-action and how do you include one responsibly?
4. Explain how your capstone can be both fun and educational.
5. Write a function that updates a conservation score based on player behaviour.
6. How do you verify the accuracy of facts shown in your project?
7. What is impact design in an educational game?
8. How would you localise conservation messages to Kiswahili?
9. What privacy concerns apply if your game collects player scores?
10. Map conservation data integration to CBE Citizenship/Data outcomes.

## Answer Key

1. import random, json
facts = json.load(open('facts.json'))
screen.draw.text(random.choice(facts), (50, 50))
2. Aggregate by region and remove exact coordinates.
3. A prompt asking the player to act, e.g., 'Learn more at KWS' with a real, safe link.
4. Gameplay mechanics reinforce real conservation facts.
5. def update_score(score, collected_plastic):
    return score + len(collected_plastic) * 10
6. Cross-check with sources like IUCN, KWS, IFAW.
7. Designing so the game produces real learning outcomes.
8. Store messages in both languages and choose based on user preference.
9. Do not collect personal identifiers without consent.
10. Learners combine evidence with advocacy in digital products.
