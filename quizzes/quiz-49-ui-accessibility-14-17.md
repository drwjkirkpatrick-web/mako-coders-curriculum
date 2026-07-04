# Week 49 Quiz — User Interface and Accessibility — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 49: User Interface and Accessibility.*

## Questions

1. Write code that draws a UI panel showing score, level, and health.
2. What are WCAG and why do they matter?
3. How would you make a game playable with only a keyboard?
4. Explain colour contrast and why it matters.
5. What is alt text and when do you use it?
6. How do you test accessibility without specialised tools?
7. Write a function that scales UI elements based on screen size.
8. What is inclusive design?
9. How would you add subtitles or captions to a game?
10. Map UI/accessibility to CBE Digital Literacy/Citizenship outcomes.

## Answer Key

1. screen.draw.filled_rect(Rect(0,0,200,60), 'black')
screen.draw.text(f'Score: {score}', (10, 10))
2. Web Content Accessibility Guidelines; they help make content usable for all.
3. Ensure all actions have keyboard controls and visible focus.
4. Sufficient contrast makes text readable for people with low vision.
5. Text description of an image; used when images cannot be seen.
6. Try using only keyboard, increase font size, or use a screen reader.
7. def ui_scale(base): return base * WIDTH / 800
8. Designing products that work for the widest range of people.
9. Display text when sounds play or speech occurs.
10. Learners design inclusive digital interfaces.
