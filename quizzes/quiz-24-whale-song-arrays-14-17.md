# Week 24 Quiz — Whale Song Arrays — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 24: Whale Song Arrays.*

## Questions

1. Write Python code to play a sequence of frequencies using simpleaudio or winsound.
2. What is the difference between a list and a NumPy array?
3. How do you compute the average frequency of a song?
4. Write code to find the highest and lowest notes.
5. What is a spectrogram?
6. Explain how arrays relate to digital audio.
7. Write a function that reverses a whale song array.
8. How would you detect repeated patterns in an array?
9. What data type should audio sample values have?
10. Map arrays to a CBE Data/Algorithms outcome.

## Answer Key

1. import winsound; for f in [200,250,300]: winsound.Beep(f, 500)
2. A NumPy array supports fast numeric operations and has a fixed type.
3. sum(notes) / len(notes)
4. max(notes), min(notes)
5. A visual representation of frequencies over time.
6. Audio is stored as a list of amplitude samples over time.
7. def reverse_song(song): return song[::-1]
8. Compare slices or use autocorrelation.
9. Integer or float, depending on bit depth.
10. Learners process sequential numeric data.
