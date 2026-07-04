# Week 42 Quiz — Classes of the Coral Reef — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 42: Classes of the Coral Reef.*

## Questions

1. Write a Python class Shark with name, x, y, and a swim() method.
2. What is encapsulation?
3. What is inheritance and how could it model sea life?
4. Explain the difference between a class attribute and an instance attribute.
5. Write code to create a list of 5 Coral objects with random colours.
6. What is polymorphism?
7. How do you override a method in Python?
8. What is __init__ used for?
9. How would you add collision detection between two objects?
10. Map classes to CBE Algorithms/Project outcomes.

## Answer Key

1. class Shark:
    def __init__(self, name, x, y):
        self.name = name; self.x = x; self.y = y
    def swim(self):
        self.x += 1
2. Keeping data and methods that operate on it together inside a class.
3. A child class gets attributes from a parent class, e.g., WhaleShark inherits Fish.
4. Class attributes are shared; instance attributes belong to one object.
5. import random; corals = [Coral(random.choice(['red','blue']), 10) for _ in range(5)]
6. Different classes responding to the same method call.
7. Define a method with the same name in the child class.
8. It sets up a new object's initial state.
9. Check if their rectangles or distance overlap.
10. Learners use object-oriented design to model complex systems.
