# Week 37 Quiz — Cybersecurity at Sea — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 37: Cybersecurity at Sea.*

## Questions

1. Write a Python function that rates a password as weak, medium, or strong.
2. What is hashing and why are passwords hashed?
3. Explain two-factor authentication in simple terms.
4. What is a man-in-the-middle attack?
5. How does HTTPS protect against this?
6. Write code to generate a random passphrase of four words.
7. What is social engineering?
8. How would you secure a classroom micro:bit network?
9. What is a firewall used for?
10. Map cybersecurity to a CBE Security outcome.

## Answer Key

1. def rate(pw):
    score = 0
    if len(pw) > 8: score += 1
    if any(c.isupper() for c in pw): score += 1
    ... return ['weak','medium','strong'][min(score,2)]
2. Hashing turns a password into a fixed value; even database leaks do not reveal the password.
3. You need two proofs of identity, like a password and a phone code.
4. An attacker secretly intercepts messages between two parties.
5. It encrypts the connection so attackers cannot read the data.
6. import random; words = ['blue','shark','reef','tide']; print(' '.join(random.sample(words,4)))
7. Tricking people into revealing secrets instead of breaking technology.
8. Use a private radio group and avoid sending sensitive data.
9. To block unwanted network traffic.
10. Learners apply safe practices to protect digital systems and data.
