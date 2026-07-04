"""
Rewrite all Mako Coders quizzes with unique, code-only, CBE-aligned questions.

Run: python3 scripts/rewrite_quizzes_code_only.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / 'tests'))
from modules import MODULES

QUIZZES_DIR = ROOT / 'quizzes'


def question_bank():
    """
    Return a dict keyed by (week, age_band) of 10 (question, answer) pairs.
    Every question is code-focused and tied to that week's concept and CBE strand.
    """
    qb = {}

    # Week 1: Digital Literacy / setup
    qb[(1, "10-13")] = [
        ("Which Scratch block starts every program when the green flag is clicked?", "Events → When [green flag] clicked."),
        ("Name the three main parts of a computer you need to set up before coding.", "Input, processing, and output."),
        ("What does the 'Save' button do?", "It stores your project so you do not lose work."),
        ("Write the first block you should always add to a new Scratch sprite.", "When green flag clicked."),
        ("Why is it important to name your project file clearly?", "So you can find it again easily."),
        ("What is an example of an input device?", "Keyboard, mouse, microphone, or touchscreen."),
        ("What is an example of an output device?", "Screen, speaker, or printer."),
        ("In one sentence, what does a coder do?", "A coder writes instructions for a computer to follow."),
        ("What happens if you turn off the computer before saving?", "Unsaved work may be lost."),
        ("List two rules for safely using a school computer.", "Do not share passwords; only open files you created or the teacher shared.")
    ]
    qb[(1, "14-17")] = [
        ("What are the five RPF Digital Making strands?", "Design, Code, Create, Connect, Evaluate."),
        ("Explain the difference between hardware and software using one example of each.", "Hardware is physical (e.g., micro:bit); software is programs (e.g., Scratch editor)."),
        ("Write the command to print 'Mako shark' in Python.", "print('Mako shark')"),
        ("Why should you keep backup copies of your project?", "To recover work if a file is deleted or corrupted."),
        ("What is the CBE 2-6-3-3 structure in Kenyan education?", "2 years pre-primary, 6 primary, 3 junior school, 3 senior school."),
        ("Name two of the seven CBE core competencies.", "Communication, Critical Thinking, Creativity, Collaboration, Digital Literacy, Citizenship, Learning to Learn."),
        ("Which HTML tag would you use to make a heading on a simple report page?", "<h1>"),
        ("What does the CPU do?", "It processes instructions from programs."),
        ("Why is a folder structure useful for coding projects?", "It groups related files and makes projects easier to navigate."),
        ("Give one example of being a responsible digital citizen while sharing code online.", "Use a clear license, give credit, and do not share private data.")
    ]

    # Week 2: Sequencing
    qb[(2, "10-13")] = [
        ("Put these Scratch blocks in order to make a turtle move to the sea: point in direction 90, move 10 steps, when green flag clicked.", "1. When green flag clicked; 2. point in direction 90; 3. move 10 steps."),
        ("What does 'sequencing' mean in coding?", "Putting instructions in the correct order."),
        ("If you swap two blocks in a sequence, what can happen?", "The sprite may move or act in the wrong way."),
        ("Which block runs first in a Scratch script?", "The block directly under the event hat (e.g., when green flag clicked)."),
        ("Write a 3-block sequence that makes a sprite say 'Hello' then wait 1 second then say 'Ocean'.", "When green flag clicked → say Hello for 2 secs → wait 1 secs → say Ocean for 2 secs."),
        ("Why must a sea-turtle animation reach the water before turning around?", "Because order matters in a sequence."),
        ("What is an algorithm?", "A step-by-step set of instructions."),
        ("How many blocks are in this sequence: event + move + turn + say?", "Four blocks."),
        ("In pseudocode, write three steps to draw a square.", "1. Move forward; 2. Turn 90 degrees; 3. Repeat four times."),
        ("What should you do after adding one new block to a script?", "Run the program and check the result.")
    ]
    qb[(2, "14-17")] = [
        ("Write Python code to move a turtle forward 100 pixels, turn left 90 degrees, and move forward 100 pixels again.", "import turtle; t = turtle.Turtle(); t.forward(100); t.left(90); t.forward(100)"),
        ("Why is a sequence's order non-negotiable for a computer?", "Computers execute instructions sequentially; changing order changes output."),
        ("Convert these Scratch blocks to pseudocode: when green flag clicked → move 10 steps → turn 15 degrees → say 'Done'.", "START; move 10; turn 15; output 'Done'; END."),
        ("What is the output of this Python sequence? x = 5; x = x + 2; print(x)", "7"),
        ("Give a real-world example of a sequence where order matters.", "Baking a cake, launching a rocket, or a medical checklist."),
        ("In a flowchart, what shape usually represents a process/step?", "Rectangle."),
        ("What happens if a 'wait' block is placed at the start instead of between actions?", "The sprite waits before doing anything else."),
        ("Write a sequence that draws an equilateral triangle using Python Turtle.", "for _ in range(3): t.forward(100); t.left(120)"),
        ("How can you test a long sequence for errors?", "Run it step by step or add temporary pause blocks."),
        ("Name the CBE strand for sequencing and give one competency it builds.", "Algorithms strand; builds logical thinking and problem solving.")
    ]

    # Week 3: Sprites & Motion
    qb[(3, "10-13")] = [
        ("Which block changes a sprite's position to a specific x and y coordinate?", "go to x: _ y: _"),
        ("What does the 'glide' block do?", "Moves a sprite smoothly to a point over time."),
        ("If a sprite is at x=0, y=0 and you use 'change x by 50', where does it go?", "To x=50, y=0."),
        ("Which block makes a sprite point towards the mouse pointer?", "point towards mouse-pointer"),
        ("Write the blocks to make a turtle sprite move in a circle.", "Repeat 12: move 10 steps, turn 30 degrees."),
        ("What is a costume in Scratch?", "A different picture for the same sprite."),
        ("How do you make a sprite flip to its next costume?", "Use the 'next costume' block."),
        ("Which Motion block reports where the sprite is?", "x position / y position"),
        ("What does 'set rotation style left-right' stop?", "It stops the sprite from rotating upside down."),
        ("Create a 5-block script that makes a hatchling turtle walk to the sea and switch costume.", "When green flag clicked → go to x:-200 y:-100 → repeat 10: move 10 steps, next costume.")
    ]
    qb[(3, "14-17")] = [
        ("Write Python Turtle code to set the turtle's position to (100, -50) without drawing.", "import turtle; t = turtle.Turtle(); t.penup(); t.setpos(100, -50)"),
        ("What is the difference between absolute and relative movement in Scratch?", "Absolute uses exact coordinates; relative uses change by/direction."),
        ("Which Python Turtle command stamps a copy of the turtle shape?", "t.stamp()"),
        ("How would you make a sprite follow the mouse pointer in Scratch?", "Forever: point towards mouse-pointer, move 5 steps."),
        ("What are the coordinates of the centre of the Scratch stage?", "x=0, y=0."),
        ("Write code to make a turtle walk forward until it touches the edge of the screen.", "while not t.xcor() > 300: t.forward(5)"),
        ("What does the 'if on edge, bounce' block do?", "It reverses direction when a sprite hits the stage edge."),
        ("Explain how costumes relate to animation frames.", "Each costume is one frame; switching quickly creates animation."),
        ("Which CBE competency is strengthened when learners debug sprite motion?", "Critical Thinking and Problem Solving."),
        ("Give the coordinate pairs for the four corners of a standard Scratch stage.", "Top-left (-240,180), top-right (240,180), bottom-right (240,-180), bottom-left (-240,-180).")
    ]

    # Week 4: Loops
    qb[(4, "10-13")] = [
        ("Which block repeats a set of actions a specific number of times?", "repeat 10"),
        ("How many times will a spinner dolphin spin if the repeat block says 8?", "8 times."),
        ("What is the difference between 'repeat' and 'forever'?", "Repeat stops after a set number; forever never stops."),
        ("Write a loop that makes a dolphin turn 360 degrees in 10 equal steps.", "Repeat 10: turn 36 degrees."),
        ("Why are loops useful in coding?", "They let you repeat code without writing it many times."),
        ("If you have 'repeat 5' around a 'move 10 steps' block, how far does the sprite move?", "50 steps."),
        ("What happens if a loop has no blocks inside it?", "Nothing repeats."),
        ("Which block category contains the repeat loops in Scratch?", "Control."),
        ("Write a script that makes a dolphin spin forever when the flag is clicked.", "When green flag clicked → forever: turn 15 degrees."),
        ("How do you stop a 'forever' loop in Scratch?", "Click the red stop sign.")
    ]
    qb[(4, "14-17")] = [
        ("Write a Python for-loop that prints the numbers 1 to 10.", "for i in range(1, 11): print(i)"),
        ("What is the difference between a for-loop and a while-loop?", "A for-loop repeats a known number of times; a while-loop repeats while a condition is true."),
        ("How many times does this loop run? for i in range(5):", "5 times (i = 0,1,2,3,4)."),
        ("Write code that uses a loop to draw a 10-sided regular polygon.", "import turtle; for _ in range(10): t.forward(40); t.left(36)"),
        ("What is an infinite loop and why should you avoid it?", "A loop that never ends; it can freeze the program."),
        ("In Scratch, how would you repeat an action until a sprite reaches the edge?", "Repeat until touching edge: do the action."),
        ("What value does the loop counter hold after 'for i in range(3)' finishes?", "The last value is 2; after the loop i is 2 in scope."),
        ("Write pseudocode for a loop that counts down from 10 to 1.", "FOR i FROM 10 DOWNTO 1: PRINT i; END FOR."),
        ("Which CBE strand connects loops to solving repetitive problems?", "Algorithms."),
        ("Explain how a loop reduces code duplication in an ocean animation.", "One move/turn block inside a repeat draws many shapes instead of many separate blocks.")
    ]

    # Week 5: Nested loops
    qb[(5, "10-13")] = [
        ("What is a nested loop?", "A loop inside another loop."),
        ("If the outer loop repeats 3 times and the inner loop repeats 4 times, how many times does the inner block run?", "12 times."),
        ("Which block would you put inside which to draw a grid of coral?", "Put the row loop inside the column loop, or vice versa."),
        ("Draw the pattern made by: repeat 2 [ repeat 3 [stamp] move 20 ] turn 90.", "Two rows of three stamps each, rotated."),
        ("Why is a nested loop useful for drawing coral reefs?", "It repeats shapes across rows and columns."),
        ("How many total stamps if repeat 4 contains repeat 5 contains stamp?", "20 stamps."),
        ("What changes between the inner loop and outer loop in a grid?", "The outer loop usually changes rows; the inner loop changes columns."),
        ("Write nested Scratch blocks to draw a 3x3 grid of coral squares.", "Repeat 3 rows: repeat 3 columns: draw square, move right; move to next row."),
        ("What happens if you forget to move the turtle between inner loops?", "The shapes overlap."),
        ("Name the CBE competency built by planning nested patterns.", "Critical Thinking / Creativity.")
    ]
    qb[(5, "14-17")] = [
        ("Write Python code for a nested loop that prints a 3x3 grid of asterisks.", "for row in range(3):\n    for col in range(3):\n        print('*', end=' ')\n    print()"),
        ("What is the time complexity of a simple nested loop where each loop runs n times?", "O(n²)."),
        ("How would you use nested loops to draw a checkerboard of coral and sand?", "Outer loop rows; inner loop columns; use (row+col) % 2 to pick colour."),
        ("Write code that draws 5 concentric circles using nested loops.", "Use an outer loop to change radius and an inner loop to draw each circle."),
        ("What is the output of this nested loop? for i in range(2): for j in range(2): print(i,j)", "0 0, 0 1, 1 0, 1 1."),
        ("Explain the difference between nested loops and a single loop that repeats twice as long.", "Nested loops combine two independent counts; a single loop has only one counter."),
        ("In a tile map, which loop index usually represents x and which y?", "Inner loop = x/columns; outer loop = y/rows."),
        ("Write a nested loop that counts how many coral tiles are in a 4x4 reef if each tile has 70% coral coverage.", "Use nested loops to count 16 tiles, then multiply by 0.7 (round to 11)."),
        ("Why must the inner loop reset its counter each time the outer loop runs?", "Otherwise it would not start a new row/column correctly."),
        ("Map nested loops to a CBE learning outcome for Algorithms.", "Learners apply repetition structures to model 2D patterns.")
    ]

    # Week 6: Conditionals
    qb[(6, "10-13")] = [
        ("Which Scratch block lets a sprite decide between two actions?", "if ... then ... else"),
        ("What does an 'if' block check?", "A condition that is true or false."),
        ("If a sprite touches a humpback dolphin, what should happen?", "Play a sound, say something, or change direction."),
        ("Which block reports whether a sprite is touching another sprite?", "touching mouse-pointer? / touching [sprite]?"),
        ("Write a conditional script: if touching edge, then bounce, else move 10.", "Forever: if touching edge then bounce else move 10 steps."),
        ("What is a Boolean value?", "A value that is either true or false."),
        ("What happens if the 'if' condition is false and there is no 'else'?", "Nothing inside the if block runs."),
        ("Which operator block checks if two numbers are equal?", "_ = _"),
        ("Give one ocean-themed condition you could test in Scratch.", "If water temperature > 25, show 'warm reef' message."),
        ("Why are conditionals useful in a dolphin identification project?", "They let the program choose different outputs based on input.")
    ]
    qb[(6, "14-17")] = [
        ("Write Python code that prints 'warm' if water_temp > 26, otherwise 'cool'.", "if water_temp > 26:\n    print('warm')\nelse:\n    print('cool')"),
        ("What is the difference between 'if', 'elif', and 'else'?", "if checks first; elif checks other conditions; else runs if none match."),
        ("Evaluate: x = 10; if x % 2 == 0: print('even'). What is printed?", "even"),
        ("Write a Scratch/Python conditional to identify a humpback dolphin by its dorsal fin shape.", "IF fin == 'small triangular' THEN species = 'humpback dolphin' ELSE 'unknown'."),
        ("What is a predicate?", "A function or expression that returns true or false."),
        ("How would you combine two conditions in Scratch?", "Use the 'and' or 'or' operator blocks."),
        ("Write code that checks if a species is endangered and native to Kenya.", "if status == 'endangered' and country == 'Kenya': print('priority')"),
        ("Explain short-circuit evaluation in a simple 'and' expression.", "If the first part is false, the second part is not checked."),
        ("What is the output? a = 5; if a < 3: print('small') elif a < 7: print('medium') else: print('large')", "medium"),
        ("Which CBE competency is developed when learners design species decision trees?", "Critical Thinking and Communication.")
    ]

    # Week 7: If-else ladders / branching
    qb[(7, "10-13")] = [
        ("What is an if-else ladder?", "Many 'if/else' checks one after another."),
        ("Why would you use more than one 'if' block in a reef project?", "To identify different species or conditions."),
        ("Put these in order: check whale shark, check turtle, check dolphin, else unknown.", "First if whale shark, elif turtle, elif dolphin, else unknown."),
        ("Which block lets you add more than one condition in Scratch?", "if ... then ... else, plus nested if blocks."),
        ("What should the final 'else' do in a species identifier?", "Say 'I do not know' or ask again."),
        ("How many branches can an if-else ladder have?", "As many as you need."),
        ("Write a ladder that chooses coral colour by depth: shallow pink, mid blue, deep purple.", "if depth < 5: pink; elif depth < 15: blue; else: purple."),
        ("What happens if two 'if' conditions are both true?", "Both blocks run unless you use if/elif."),
        ("Why is the order of conditions important in a ladder?", "Earlier conditions catch cases first."),
        ("Give one real-world use of branching in ocean technology.", "A buoy turns red light on at night, green light by day.")
    ]
    qb[(7, "14-17")] = [
        ("Write a Python function that returns the reef zone for a given depth.", "def reef_zone(depth):\n    if depth < 5: return 'shallow'\n    elif depth < 20: return 'fore-reef'\n    else: return 'deep'"),
        ("When should you use if-elif-else instead of many independent ifs?", "When only one branch should run."),
        ("What is the bug in this ladder? if x > 5: ... elif x > 10: ...", "The second condition will never run because the first catches all x > 5, including > 10."),
        ("Convert this to a dictionary lookup: if species == 'dolphin': return 2; elif species == 'shark': return 5; else: return 0.", "{ 'dolphin': 2, 'shark': 5 }.get(species, 0)"),
        ("Write a ladder that assigns protection level based on IUCN status.", "if status == 'CR': return 'urgent'; elif status == 'EN': return 'high'; elif status == 'VU': return 'medium'; else: return 'low'"),
        ("What is fall-through and how do you prevent it in Python?", "Fall-through runs multiple branches; use elif to prevent it."),
        ("Explain how branching supports adaptive learning software.", "The program changes difficulty based on the learner's score."),
        ("Which Boolean expression is true only when depth is between 5 and 15?", "depth >= 5 and depth <= 15"),
        ("How do you handle invalid user input in a branching program?", "Add an else/default branch that asks again or shows an error."),
        ("Map if-else ladders to a CBE learning outcome in the Algorithms strand.", "Learners select appropriate control structures for multi-way decisions.")
    ]

    # Week 8: Variables
    qb[(8, "10-13")] = [
        ("What is a variable?", "A box that holds a value that can change."),
        ("Which Scratch block makes a variable?", "Make a Variable"),
        ("Write the blocks to set 'score' to 0 when the flag is clicked.", "When green flag clicked → set score to 0."),
        ("What happens when you use 'change score by 1'?", "The score variable increases by 1."),
        ("Name three things you could store in a variable for a whale shark game.", "Score, health, speed, level."),
        ("Why is a variable better than writing the number 100 directly in many places?", "You can change it in one place."),
        ("What block shows a variable's value on the stage?", "show variable [score]"),
        ("If 'plankton' starts at 20 and you 'change plankton by -3', what is the new value?", "17."),
        ("Write a script that counts how many times a sprite is clicked.", "When sprite clicked → change clicks by 1."),
        ("What type of value does a score variable usually hold?", "A number.")
    ]
    qb[(8, "14-17")] = [
        ("Write Python code that creates a variable called 'filtered' and sets it to 0.", "filtered = 0"),
        ("What is the difference between a variable and a constant?", "A variable can change; a constant stays the same."),
        ("Predict the output: count = 5; count += 3; print(count)", "8"),
        ("Explain variable scope in a simple Python function.", "Variables created inside a function are local; variables outside are global."),
        ("Write code that swaps the values of a and b without a temporary variable.", "a, b = b, a"),
        ("Which Python data type would you use for a score that can be a decimal?", "float"),
        ("What is type casting and why would you use it?", "Converting a value from one type to another, e.g., int('5') for calculations."),
        ("Write a function that returns the average of three test scores.", "def average(a,b,c): return (a+b+c)/3"),
        ("How do you name variables clearly in Python?", "Use lowercase_with_underscores and meaningful names."),
        ("Which CBE strand most directly uses variables for collecting data?", "Data.")
    ]

    # Week 9: Events
    qb[(9, "10-13")] = [
        ("What is an event in Scratch?", "Something that triggers a script, like a click or key press."),
        ("Which block runs when you press the space key?", "When [space] key pressed"),
        ("What event starts a program automatically?", "When green flag clicked"),
        ("Write a script that makes a dolphin jump when the up arrow is pressed.", "When up arrow pressed → change y by 20, wait, change y by -20."),
        ("What is a message broadcast?", "A signal sent to all sprites to start a script."),
        ("Which block sends a broadcast?", "broadcast [message1]"),
        ("Which block receives a broadcast?", "When I receive [message1]"),
        ("Why are events useful for making games?", "They let the player control the program."),
        ("Name two events besides key presses in Scratch.", "Sprite clicked, backdrop switched, loudness, timer."),
        ("What happens when two scripts respond to the same event?", "Both scripts run at the same time.")
    ]
    qb[(9, "14-17")] = [
        ("Write Python code that prints 'splash' when the user presses Enter.", "Use input('Press Enter to continue...'); print('splash')"),
        ("What is an event-driven program?", "A program that waits for events like clicks or messages and then reacts."),
        ("In Pygame Zero, what function runs when the mouse is clicked?", "def on_mouse_down(): ..."),
        ("Explain the difference between polling and event handling.", "Polling repeatedly checks a state; event handling reacts only when something happens."),
        ("Write a micro:bit handler that shows a fish when button A is pressed.", "from microbit import *\ndef on_button_a(): display.show(Image.FISH)"),
        ("What is a callback function?", "A function that runs automatically when an event occurs."),
        ("How would you handle both a key press and a mouse click in one program?", "Register separate event handlers for each."),
        ("Give an example of broadcast usage in a multi-sprite ocean scene.", "When dolphin is clicked, broadcast 'splash' so all fish swim away."),
        ("What problem can occur if two events modify the same variable at the same time?", "A race condition can cause incorrect values."),
        ("Which CBE competency is strengthened by designing interactive user controls?", "Digital Literacy and Creativity.")
    ]

    # Week 10: Debugging
    qb[(10, "10-13")] = [
        ("What is debugging?", "Finding and fixing mistakes in code."),
        ("What is a bug?", "A mistake in a program."),
        ("If a mangrove sprite moves the wrong way, what is the first thing to check?", "The direction/turn value."),
        ("Which block helps you slow down a script to see what happens?", "Wait 1 secs"),
        ("What does it mean to 'test one change at a time'?", "Change only one thing before running again."),
        ("What should you do before fixing a bug?", "Find where the problem starts."),
        ("Name two common causes of a sprite not moving.", "Wrong costume centre, no motion block, or hidden."),
        ("How can you tell if a loop is running too many times?", "Check the number in the repeat block."),
        ("Write the steps you would follow when a script does not start.", "1. Check the event hat; 2. Check block order; 3. Run step by step."),
        ("Why is it important to save before debugging?", "So you can go back to a working version.")
    ]
    qb[(10, "14-17")] = [
        ("What is the difference between a syntax error and a runtime error?", "Syntax error breaks language rules; runtime error occurs while running."),
        ("What Python error appears when you use a variable before defining it?", "NameError"),
        ("How do you use print() for debugging?", "Add print() statements to show variable values at different points."),
        ("What is a stack trace and why is it useful?", "It shows the sequence of function calls that led to an error."),
        ("Write a try/except block that handles dividing by zero.", "try:\n    x = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')"),
        ("Explain rubber-duck debugging.", "Explaining your code out loud to an object helps you spot mistakes."),
        ("What is a breakpoint?", "A marker that pauses execution at a specific line so you can inspect state."),
        ("Why should tests be small and focused?", "They isolate bugs and prove one thing at a time."),
        ("Which debugging strategy would you use if a loop gives unexpected values?", "Print the loop counter each iteration."),
        ("Which CBE competency is most developed by systematic debugging?", "Critical Thinking and Problem Solving.")
    ]

    # Week 11: Decomposition
    qb[(11, "10-13")] = [
        ("What does 'decomposition' mean?", "Breaking a big problem into smaller parts."),
        ("Give the four main steps in a turtle rescue project.", "Find turtle, check health, move safely, release to sea."),
        ("Why is it easier to code small parts instead of one giant script?", "Each part is simpler to understand and test."),
        ("Which Scratch block helps you reuse a small script?", "My Blocks / Make a Block."),
        ("Name two sub-tasks of 'build an ocean scene'.", "Add background, add sprites, animate movement."),
        ("What is a sub-task?", "A small job that is part of a bigger job."),
        ("How would you decompose making a game?", "Design, code, test, share."),
        ("Write three sub-tasks for a beach-cleanup animation.", "1. Move character; 2. Pick up trash; 3. Update score."),
        ("What do you do after decomposing a problem?", "Solve each sub-task, then combine them."),
        ("Which CBE strand uses decomposition to plan algorithms?", "Algorithms.")
    ]
    qb[(11, "14-17")] = [
        ("Define decomposition in computational thinking.", "Breaking a complex problem into smaller, manageable sub-problems."),
        ("How does decomposition differ from abstraction?", "Decomposition splits into parts; abstraction hides unnecessary detail."),
        ("Write a top-level pseudocode plan for a turtle rescue app.", "1. Load map; 2. Locate turtle; 3. Assess danger; 4. Plan route; 5. Execute rescue; 6. Report."),
        ("Why should functions be small and single-purpose?", "They are easier to test, reuse, and read."),
        ("Decompose the task 'draw a Kenya marine food web' into at least four functions.", "draw_producer(), draw_primary_consumer(), draw_predator(), draw_arrows()."),
        ("What is a driver function?", "A function that calls other functions in the right order."),
        ("How would you decompose a 52-week curriculum database?", "Students table, quizzes table, attempts table, badges table."),
        ("Give one sign that a function is doing too much.", "It is very long or its name includes 'and'."),
        ("What is the relationship between decomposition and modularity?", "Decomposition produces modules that can be developed independently."),
        ("Map decomposition to a CBE learning outcome.", "Learners break complex conservation tasks into algorithmic steps.")
    ]

    # Week 12: Creativity / Ocean Scene Sprint
    qb[(12, "10-13")] = [
        ("What is a sprint in project work?", "A short burst of focused work to build something."),
        ("Name three ocean sprites you could include in a scene.", "Dolphin, turtle, coral, fish, whale shark."),
        ("Which block changes the backdrop?", "switch backdrop to [underwater]"),
        ("How do you make a sprite move automatically without the player clicking?", "Use a forever loop or an event hat."),
        ("Write a one-sentence plan for your ocean scene.", "My scene shows a turtle swimming past coral while fish move in a loop."),
        ("What makes a scene visually interesting?", "Different sprites, colours, movement, and a clear background."),
        ("How can sound improve an ocean scene?", "Add ocean or animal sounds."),
        ("Which CBE competency is strongest in a creative sprint?", "Creativity and Communication."),
        ("How do you share your scene with a classmate?", "Save the file or share a link/screenshot."),
        ("What should you test before showing your scene?", "That all sprites move as planned.")
    ]
    qb[(12, "14-17")] = [
        ("What is iterative design?", "Building, testing, and improving a project in repeated cycles."),
        ("Write Python Turtle code that draws a simple underwater scene with three different shapes.", "Use t.circle(), t.forward(), and t.color() with loops."),
        ("How do you give constructive feedback on a peer's project?", "Say what works, then suggest one specific improvement."),
        ("What is a design constraint?", "A rule or limit the project must follow, e.g., no external images."),
        ("Explain the difference between form and function in a game.", "Form is how it looks; function is what it does."),
        ("How would you use randomness to make an ocean scene feel alive?", "Random positions, sizes, or speeds for fish."),
        ("Write a function that draws a random school of fish.", "def draw_fish_school(n):\n    for _ in range(n):\n        t.goto(random.randint(-200,200), random.randint(-100,100))\n        t.stamp()"),
        ("What is a prototype?", "A quick early version used to test ideas."),
        ("How do you balance creativity with CBE learning outcomes?", "Make sure the creative choice still demonstrates the target competency."),
        ("Which CBE strand connects a creative sprint to self-expression?", "Creativity / Communication.")
    ]

    # Week 13: Showcase / Reflection
    qb[(13, "10-13")] = [
        ("What is one project you built this term?", "[Teacher checks: student names one project]"),
        ("What is one coding word you learned?", "Sequence, loop, variable, event, conditional."),
        ("How do you explain your project to someone who did not see it?", "Say what it does and how you made it."),
        ("What is one thing you want to improve next term?", "[Teacher checks: student-specific goal]"),
        ("Why is it important to listen to feedback?", "It helps you improve your project."),
        ("What did you do when your code did not work?", "[Teacher checks: debugging strategy]"),
        ("Name one thing you are proud of from this term.", "[Teacher checks: student-specific pride point]"),
        ("What tool will you use next term?", "Python + Turtle."),
        ("How do you know if a project is ready to share?", "It runs without errors and others can understand it."),
        ("Which CBE competency did you use when presenting?", "Communication.")
    ]
    qb[(13, "14-17")] = [
        ("Write three reflection questions you would ask yourself after finishing a project.", "Did I meet the brief? What worked? What would I change?"),
        ("How do you document a project so someone else can run it?", "Write a README with setup steps, file list, and example usage."),
        ("What is a retrospective?", "A meeting where a team reviews what went well and what to improve."),
        ("Give two metrics you could use to judge a coding project.", "Correctness, usability, creativity, efficiency, readability."),
        ("How would you compare Scratch and Python for teaching coding?", "Scratch is visual; Python is text-based and more powerful."),
        ("What is technical debt?", "Shortcuts in code that may cause problems later."),
        ("How do you prioritise improvements for a project?", "Fix bugs first, then add features, then polish."),
        ("Explain how presenting your project builds a CBE competency.", "It builds Communication and Collaboration."),
        ("What would you add to your Term 1 project if you had more time?", "[Teacher checks: specific improvement]"),
        ("Why is self-assessment important in CBE?", "Learners take ownership of their learning progress.")
    ]

    # Week 14: Blocks to Text
    qb[(14, "10-13")] = [
        ("What does 'blocks to text' mean?", "Moving from Scratch blocks to typed code."),
        ("Which programming language will we use next?", "Python."),
        ("Write the Python version of 'say Hello for 2 secs'.", "print('Hello')"),
        ("What is a text editor?", "A program where you type code."),
        ("Which is longer: a Scratch script or the same program in Python?", "Python is usually shorter and uses words instead of blocks."),
        ("What must you remember when typing Python instead of dragging blocks?", "Spelling, indentation, and punctuation matter."),
        ("Write the Python version of 'repeat 10: move 10 steps'.", "for _ in range(10):\n    t.forward(10)"),
        ("What happens if you forget a colon (:) at the end of a Python line?", "You get a syntax error."),
        ("Why is indentation important in Python?", "It shows which lines belong to a loop or condition."),
        ("Which CBE strand links blocks-to-text transition?", "Digital Literacy.")
    ]
    qb[(14, "14-17")] = [
        ("Convert this Scratch block to Python: set x to 0.", "x = 0"),
        ("Convert this Scratch block to Python: repeat until touching edge.", "while not touching_edge():\n    move()"),
        ("What is a REPL?", "Read-Eval-Print Loop — an interactive coding environment."),
        ("Why is Python case-sensitive?", "Variable names like 'score' and 'Score' are different."),
        ("What is the difference between an interpreted and a compiled language?", "Interpreted runs line by line; compiled is translated to machine code first."),
        ("Write the Python equivalent of 'if x > 10 then say big else say small'.", "if x > 10:\n    print('big')\nelse:\n    print('small')"),
        ("What is a syntax error and how is it shown?", "A mistake in grammar; Python prints a red error message."),
        ("Why are comments useful when switching from blocks to text?", "They explain what the code does in words."),
        ("Write a Python comment that describes a loop.", "# Move the turtle in a circle"),
        ("Map the blocks-to-text transition to a CBE Digital Literacy outcome.", "Learners use multiple coding environments to solve problems.")
    ]

    # Week 15: Data types
    qb[(15, "10-13")] = [
        ("What is a string?", "Text, like 'whale shark'."),
        ("What is a number called in programming?", "An integer or float."),
        ("Which data type would you use for a species name?", "String."),
        ("Which data type would you use for a shark's length in metres?", "Number/float."),
        ("What does this code do? length = 12", "It stores the number 12 in a variable called length."),
        ("What is a Boolean?", "A value that is True or False."),
        ("Give one example of True/False data in an ocean project.", "is_endangered = True."),
        ("What happens if you try to add a string and a number?", "You get a type error."),
        ("Write code that stores the name of a whale shark in a variable.", "species = 'whale shark'"),
        ("Which CBE strand focuses on data types?", "Data.")
    ]
    qb[(15, "14-17")] = [
        ("Name Python's three basic data types and give an example of each.", "int (5), float (5.5), str ('shark'), bool (True)"),
        ("What is type checking and why is it useful?", "Verifying the kind of value a variable holds to prevent errors."),
        ("What is the output of type(12.0) in Python?", "<class 'float'>"),
        ("Write code that safely converts user input to an integer.", "age = int(input('Enter age: '))"),
        ("What is the difference between '5' and 5 in Python?", "'5' is a string; 5 is an integer."),
        ("Explain why mixing types in arithmetic can cause bugs.", "Adding a string to a number raises a TypeError."),
        ("What data type would you use for a GPS coordinate like -4.05?", "float"),
        ("Write a Python expression that checks if a species string starts with 'whale'.", "species.startswith('whale')"),
        ("How would you store a true/false flag for 'tagged'?", "tagged = False"),
        ("Map data types to a CBE Data strand outcome.", "Learners select appropriate data types for real-world measurements.")
    ]

    # Week 16: Lists
    qb[(16, "10-13")] = [
        ("What is a list?", "A container that holds many values in order."),
        ("Write a list of three Kenyan marine species.", "['spinner dolphin', 'green turtle', 'whale shark']"),
        ("How do you get the first item of a list?", "list_name[0]"),
        ("What number does Python use for the first item in a list?", "0"),
        ("How do you add an item to a list?", "Use append()."),
        ("Write code to add 'dugong' to a list called species.", "species.append('dugong')"),
        ("How many items are in this list? ['shark', 'turtle', 'fish', 'coral']", "4"),
        ("What is the last index of a list with 5 items?", "4"),
        ("Why are lists useful for Kenyan marine life data?", "They store many species in one variable."),
        ("Which CBE strand uses lists?", "Data.")
    ]
    qb[(16, "14-17")] = [
        ("Write a Python list that holds 5 real Kenyan ocean species.", "species = ['spinner_dolphin', 'green_turtle', 'whale_shark', 'dugong', 'humpback_dolphin']"),
        ("What is list indexing and slicing?", "Indexing gets one item; slicing gets a range of items."),
        ("What does species[2:4] return for a 5-item list?", "Items at index 2 and 3."),
        ("How do you insert an item at the start of a list?", "species.insert(0, 'new_item')"),
        ("Write code to remove the last item from a list and store it.", "last = species.pop()"),
        ("What is the difference between append() and extend()?", "append() adds one item; extend() adds multiple items."),
        ("How do you check if 'mako' is in a list?", "'mako' in species"),
        ("Explain list mutation with an example.", "species[0] = 'mako' changes the first item."),
        ("Write a loop that prints every species in a list.", "for s in species:\n    print(s)"),
        ("Map lists to a CBE Data strand outcome.", "Learners store and manipulate ordered collections of data.")
    ]

    # Week 17: Filtering data
    qb[(17, "10-13")] = [
        ("What does filtering mean?", "Keeping only the items that match a rule."),
        ("If you filter species by 'starts with s', which would you keep: shark, turtle, seahorse, dolphin?", "shark, seahorse."),
        ("Which Python word checks every item in a list?", "for"),
        ("Write code that prints only species with length > 5 metres.", "for s in species:\n    if length[s] > 5:\n        print(s)"),
        ("What do you need before filtering a list?", "A condition to test each item."),
        ("Why would you filter plankton data?", "To find only the large samples or only the ones from Kenya."),
        ("What happens if no items match the filter?", "The result list is empty."),
        ("Name one filter you could apply to a list of sea animals.", "Endangered, carnivore, or coastal."),
        ("Which block in Scratch could you use to filter?", "A repeat + if combination."),
        ("Which CBE strand connects to filtering?", "Data.")
    ]
    qb[(17, "14-17")] = [
        ("Write a Python list comprehension that keeps only species longer than 3 metres.", "big = [s for s in species if lengths[s] > 3]"),
        ("What is the difference between filtering and sorting a list?", "Filtering removes items; sorting reorders them."),
        ("Write a function filter_endangered(species, status) that returns only endangered species.", "def filter_endangered(species, status):\n    return [s for s in species if status[s] == 'endangered']"),
        ("How do you filter a dictionary by value?", "Use a dict comprehension: {k:v for k,v in d.items() if v > threshold}"),
        ("What is the output of [x for x in [1,2,3,4] if x % 2 == 0]?", "[2, 4]"),
        ("Explain why filtering is a form of abstraction.", "It hides the items that do not match, leaving only what matters."),
        ("Write code that filters a DataFrame for rows where country == 'Kenya'.", "df[df['country'] == 'Kenya']"),
        ("What is a predicate in filtering?", "A function that returns True or False for each item."),
        ("How would you test a filter function?", "Give it a small list with known matches and non-matches."),
        ("Map filtering to a CBE Data strand outcome.", "Learners extract relevant data using conditions.")
    ]

    # Week 18: Coordinates
    qb[(18, "10-13")] = [
        ("What is a coordinate pair?", "An x value and a y value that locate a point."),
        ("What is the centre of the Scratch stage?", "x=0, y=0."),
        ("If a seagrass bed is at (50, -30), is it above or below centre?", "Below centre."),
        ("Which direction is positive x on a standard stage?", "Right."),
        ("Which direction is positive y on a standard stage?", "Up."),
        ("Write the coordinates for a point in the top-right corner of the stage.", "(240, 180) in Scratch."),
        ("How do you move a sprite to a specific point?", "go to x: _ y: _"),
        ("What does the y coordinate tell you?", "How far up or down a point is."),
        ("Name one ocean feature you could place using coordinates.", "Coral reef, seagrass bed, or mangrove."),
        ("Which CBE strand uses coordinates?", "Data / Algorithms.")
    ]
    qb[(18, "14-17")] = [
        ("Write Python code to plot a point at latitude -4.0 and longitude 39.5.", "import matplotlib.pyplot as plt; plt.scatter(39.5, -4.0)"),
        ("What is the difference between Cartesian and geographic coordinates?", "Cartesian uses x/y; geographic uses latitude/longitude."),
        ("How would you store many coordinate points in Python?", "As a list of tuples: points = [(39.5, -4.0), (40.1, -3.8)]"),
        ("Write a loop that draws a dot at each coordinate in a list.", "for x, y in points:\n    plt.scatter(x, y)"),
        ("What is a bounding box?", "The rectangle defined by minimum and maximum coordinates."),
        ("How do you check if a point is inside a rectangle?", "Check x between left/right and y between bottom/top."),
        ("Explain how coordinates relate to arrays in image processing.", "Each pixel has an (x,y) position and a colour value."),
        ("Write a function distance(x1, y1, x2, y2) using the Pythagorean theorem.", "import math; return math.sqrt((x2-x1)**2 + (y2-y1)**2)"),
        ("What projection challenge occurs when mapping a sphere to a flat screen?", "Distortion of size/shape near the poles."),
        ("Map coordinate systems to a CBE Data/Algorithms outcome.", "Learners represent and use positional data in computational models.")
    ]

    # Week 19: Dictionaries
    qb[(19, "10-13")] = [
        ("What is a dictionary?", "A collection of key-value pairs."),
        ("Write a dictionary that stores a dugong's name and length.", "dugong = {'name': 'Dottie', 'length': 3}"),
        ("How do you get the value for a key?", "dictionary['key']"),
        ("What happens if you ask for a key that is not in the dictionary?", "You get an error unless you use .get()."),
        ("How do you add a new key to a dictionary?", "dictionary['new_key'] = value"),
        ("Which data type would you use for the key?", "Usually a string."),
        ("Give one real-world use of a dictionary for marine life.", "Store species names with their conservation status."),
        ("Write code to print the length of a dugong from a dictionary.", "print(dugong['length'])"),
        ("What is the difference between a list and a dictionary?", "A list uses numbers; a dictionary uses keys."),
        ("Which CBE strand uses dictionaries?", "Data.")
    ]
    qb[(19, "14-17")] = [
        ("Write a Python dictionary that maps three Kenyan species to their IUCN status.", "status = {'mako': 'VU', 'green_turtle': 'EN', 'whale_shark': 'EN'}"),
        ("What is a key-value pair?", "A key that identifies an item and a value that stores its data."),
        ("How is a dictionary implemented in Python?", "As a hash table for fast key lookup."),
        ("Write code that safely reads a value, defaulting to 'unknown' if the key is missing.", "status.get('dugong', 'unknown')"),
        ("How do you loop over both keys and values?", "for species, st in status.items(): ..."),
        ("What makes a dictionary key valid?", "It must be hashable, like a string, number, or tuple."),
        ("Write a dictionary comprehension that counts letters in a word.", "{letter: word.count(letter) for letter in set(word)}"),
        ("Explain when to use a dict instead of a list.", "Use a dict for labelled lookup; use a list for ordered sequences."),
        ("How would you merge two dictionaries?", "Use update() or {**a, **b}."),
        ("Map dictionaries to a CBE Data strand outcome.", "Learners store and retrieve structured data using labelled keys.")
    ]

    # Week 20: Functions
    qb[(20, "10-13")] = [
        ("What is a function?", "A named block of code that does one job."),
        ("Why are functions useful?", "You can reuse code without rewriting it."),
        ("Write a Scratch custom block called draw_fish.", "Make a Block: define draw_fish; inside: draw shape."),
        ("What does it mean to 'call' a function?", "To run the code inside it."),
        ("How many times can you call a function?", "As many times as you like."),
        ("Write pseudocode for a function that draws a school of 5 fish.", "define draw_school:\n    repeat 5: draw_fish, move right."),
        ("What is an input to a function called?", "A parameter or argument."),
        ("If a function needs a colour, how do you give it one?", "Pass it as a parameter."),
        ("Name one thing you could put in a function for an ocean project.", "Draw a fish, move a shark, play a sound."),
        ("Which CBE strand links to functions?", "Algorithms.")
    ]
    qb[(20, "14-17")] = [
        ("Write a Python function called draw_fish(size) that prints a simple fish shape.", "def draw_fish(size):\n    print('<' + '-'*size + '><')"),
        ("What is the difference between a parameter and an argument?", "A parameter is in the definition; an argument is the value passed in."),
        ("What does return do in a function?", "It sends a value back to the caller."),
        ("Write a function that returns the bigger of two numbers.", "def bigger(a, b):\n    return a if a > b else b"),
        ("What is a side effect?", "Something a function does besides returning a value, like printing."),
        ("Explain why functions improve maintainability.", "Changes only need to happen in one place."),
        ("Write a function that calculates the area of a reef given width and length.", "def reef_area(w, l): return w * l"),
        ("What is recursion?", "A function that calls itself."),
        ("Write a recursive function to count down from n to 1.", "def countdown(n):\n    if n <= 0: return\n    print(n); countdown(n-1)"),
        ("Map functions to a CBE Algorithms outcome.", "Learners design reusable procedures to solve sub-problems.")
    ]

    # Week 21: Timers / Data
    qb[(21, "10-13")] = [
        ("Which Scratch block tells you how much time has passed?", "timer"),
        ("How do you reset the timer in Scratch?", "reset timer"),
        ("What unit does the Scratch timer use?", "Seconds."),
        ("Write a script that starts a timer when the flag is clicked and stops when the turtle nests.", "When green flag clicked: reset timer. When turtle reaches sand: say timer."),
        ("Why would you time a turtle nesting?", "To measure how long the turtle spends on the beach."),
        ("What block waits for a number of seconds?", "wait _ secs"),
        ("If the timer says 45, how many minutes is that?", "0.75 minutes or 45 seconds."),
        ("How do you store the timer value in a variable?", "set [nest_time] to timer"),
        ("Name one real-world use of a timer in conservation.", "Measuring dive times or nesting durations."),
        ("Which CBE strand links timers and data?", "Data.")
    ]
    qb[(21, "14-17")] = [
        ("Write Python code to wait for 2 seconds.", "import time; time.sleep(2)"),
        ("How do you record the current time in Python?", "import time; start = time.time()"),
        ("Write code that prints how long a block of code took to run.", "start = time.time(); ...; print(time.time() - start)"),
        ("What is epoch time?", "Seconds since 1 January 1970."),
        ("How would you format a timestamp into a readable date?", "import datetime; datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')"),
        ("Explain why timestamps are important in data logging.", "They show exactly when each measurement was taken."),
        ("Write a function that returns True if a turtle nesting took longer than 2 hours.", "def long_nest(seconds): return seconds > 7200"),
        ("What is the difference between time.sleep() and a busy-wait loop?", "sleep() pauses efficiently; busy-waste wastes CPU."),
        ("How would you schedule a script to run every hour?", "Use a loop with time.sleep(3600) or a scheduler like cron."),
        ("Map timers and timestamps to a CBE Data outcome.", "Learners record and use time-based data.")
    ]

    # Week 22: Survey data
    qb[(22, "10-13")] = [
        ("What is a survey?", "A way of collecting data by asking questions or counting things."),
        ("Give one way to collect data about marine animals.", "Aerial photos, beach patrols, or interviews."),
        ("What does a table of data usually have?", "Rows and columns."),
        ("If a survey counted 12 turtles and 5 dolphins, what is the total?", "17 animals."),
        ("How do you find the biggest number in a list?", "Use max()."),
        ("Write code to count how many whale sharks were seen if sightings = [3, 0, 2, 5].", "sum(sightings)"),
        ("What does 'total' mean in a survey?", "The sum of all counts."),
        ("Why is it important to record where and when data was collected?", "So the data can be trusted and compared."),
        ("Name one way to show survey results.", "A bar chart or table."),
        ("Which CBE strand connects surveys and data?", "Data.")
    ]
    qb[(22, "14-17")] = [
        ("How would you store 2023 aerial survey data in Python?", "As a CSV file or a list of dictionaries."),
        ("Write Python code to read a CSV file using the standard library.", "import csv; rows = list(csv.reader(open('survey.csv')))"),
        ("What is the difference between a sample and a population in a survey?", "A population is all items; a sample is a subset."),
        ("How do you calculate the average sightings per day from a list?", "sum(sightings) / len(sightings)"),
        ("Write code to find the day with the most sightings.", "max(sightings)"),
        ("What is a pandas DataFrame and why is it useful?", "A 2D table structure with labels; good for analysis."),
        ("Explain why data cleaning is important.", "Errors or missing values can make analysis wrong."),
        ("Write code to filter survey rows where species == 'whale_shark'.", "df[df['species'] == 'whale_shark']"),
        ("What is metadata? Give an example.", "Data about data, e.g., date, location, observer name."),
        ("Map survey data to a CBE Data outcome.", "Learners collect, clean, and summarise real-world data sets.")
    ]

    # Week 23: Plotting
    qb[(23, "10-13")] = [
        ("What is a bar chart?", "A chart with bars showing amounts."),
        ("Which Python library can draw charts?", "matplotlib"),
        ("Write code to draw a bar of height 8.", "import matplotlib.pyplot as plt; plt.bar('Turtles', 8); plt.show()"),
        ("What goes on the x-axis of a chart?", "Categories or labels."),
        ("What goes on the y-axis of a chart?", "Numbers or values."),
        ("Name two chart types you can use for survey data.", "Bar chart and line graph."),
        ("Why is a chart better than a big list of numbers?", "It helps you see patterns quickly."),
        ("What does plt.show() do?", "Displays the chart on screen."),
        ("How do you add a title to a chart?", "plt.title('Kenya Marine Sightings')"),
        ("Which CBE strand links to plotting?", "Data.")
    ]
    qb[(23, "14-17")] = [
        ("Write code to plot a line graph of turtle sightings over 7 days.", "plt.plot(days, sightings); plt.xlabel('Day'); plt.ylabel('Sightings'); plt.show()"),
        ("What is the difference between plt.plot() and plt.scatter()?", "plot connects points; scatter shows individual points."),
        ("How do you save a chart to a file instead of showing it?", "plt.savefig('chart.png')"),
        ("Explain why adding labels and titles matters.", "It makes the chart readable and trustworthy."),
        ("Write code to plot multiple species on the same chart.", "plt.plot(days, dolphins, label='Dolphins'); plt.plot(days, turtles, label='Turtles'); plt.legend()"),
        ("What is a histogram used for?", "Showing how often values fall into ranges."),
        ("How would you handle missing data before plotting?", "Skip the missing point or use a placeholder/mean."),
        ("Write code to set the colour of a bar chart.", "plt.bar(species, counts, color=['blue','green','red'])"),
        ("What is a misleading graph and how do you avoid it?", "A graph that distorts scale or omits context; use clear labels and consistent scales."),
        ("Map plotting to a CBE Data outcome.", "Learners visualise data to identify patterns and communicate findings.")
    ]

    # Week 24: Arrays / whale song
    qb[(24, "10-13")] = [
        ("What is an array?", "A list of values, often all of the same type."),
        ("Write a list of 5 whale song notes.", "notes = [200, 250, 300, 250, 200]"),
        ("How do you play the first note?", "notes[0]"),
        ("What does len(notes) tell you?", "How many notes are in the list."),
        ("How do you change the third note?", "notes[2] = 400"),
        ("Write a loop that prints every note.", "for note in notes: print(note)"),
        ("What could the numbers in a whale song list represent?", "Frequencies or pitches."),
        ("How do you add a new note to the end?", "notes.append(350)"),
        ("Name one thing you could visualise from a whale song array.", "A bar graph of note heights."),
        ("Which CBE strand connects arrays and sound?", "Data / Creativity.")
    ]
    qb[(24, "14-17")] = [
        ("Write Python code to play a sequence of frequencies using simpleaudio or winsound.", "import winsound; for f in [200,250,300]: winsound.Beep(f, 500)"),
        ("What is the difference between a list and a NumPy array?", "A NumPy array supports fast numeric operations and has a fixed type."),
        ("How do you compute the average frequency of a song?", "sum(notes) / len(notes)"),
        ("Write code to find the highest and lowest notes.", "max(notes), min(notes)"),
        ("What is a spectrogram?", "A visual representation of frequencies over time."),
        ("Explain how arrays relate to digital audio.", "Audio is stored as a list of amplitude samples over time."),
        ("Write a function that reverses a whale song array.", "def reverse_song(song): return song[::-1]"),
        ("How would you detect repeated patterns in an array?", "Compare slices or use autocorrelation."),
        ("What data type should audio sample values have?", "Integer or float, depending on bit depth."),
        ("Map arrays to a CBE Data/Algorithms outcome.", "Learners process sequential numeric data.")
    ]

    # Week 25: Data ethics
    qb[(25, "10-13")] = [
        ("What is private data?", "Information that should not be shared with everyone."),
        ("Give one example of private wildlife data.", "Exact nesting beach location."),
        ("Why should you not share passwords?", "Others could pretend to be you."),
        ("What should you do before posting a photo of someone online?", "Ask permission."),
        ("Why is it important to give credit when using someone else's data?", "It respects their work."),
        ("What is one rule for safe online behaviour?", "Do not share personal information."),
        ("Who owns data collected by a research project?", "The people or organisation that collected it, with community consent."),
        ("What does 'consent' mean?", "Permission to use data or images."),
        ("Why should wildlife locations stay private?", "To protect animals from poaching or disturbance."),
        ("Which CBE strand links to data ethics?", "Citizenship.")
    ]
    qb[(25, "14-17")] = [
        ("What is informed consent in data collection?", "People understand and agree to how their data will be used."),
        ("Explain the principle of data minimisation.", "Collect only the data you actually need."),
        ("How can sharing GPS coordinates harm wildlife?", "Poachers or tourists can find sensitive habitats."),
        ("What is anonymisation?", "Removing information that identifies a person or exact location."),
        ("Write a short data-use policy for a Kenyan marine app.", "We collect only species counts, no exact locations, and share summaries only with researchers."),
        ("What is a Creative Commons license used for?", "To tell others how they may use your work."),
        ("How should you handle community knowledge about fishing spots?", "Ask permission and protect sensitive details."),
        ("What is the difference between open data and private data?", "Open data can be freely shared; private data has access restrictions."),
        ("Explain GDPR-style rights in simple terms.", "People have the right to know, correct, and delete their data."),
        ("Map data ethics to a CBE Citizenship outcome.", "Learners use technology responsibly and respect privacy.")
    ]

    # Week 26: Mini-project
    qb[(26, "10-13")] = [
        ("What is the first step in building a mini-project?", "Plan what it will do."),
        ("Name two Python tools you could use in your Marine Data Explorer.", "Lists, dictionaries, matplotlib."),
        ("What should your project show about Kenyan marine life?", "Data such as species counts or locations."),
        ("How do you know if your project works?", "You run it and check the output."),
        ("What is one thing to add to make your project easier to use?", "Labels, instructions, or a menu."),
        ("Why is testing important before sharing?", "To find bugs."),
        ("Name one chart you could include.", "Bar chart of species counts."),
        ("What is a feature?", "One thing the program can do."),
        ("How do you save a chart image?", "plt.savefig('chart.png')"),
        ("Which CBE strand links a data mini-project?", "Data / Creativity.")
    ]
    qb[(26, "14-17")] = [
        ("Write a short design brief for a Marine Data Explorer app.", "The app lets users view, filter, and chart Kenyan marine species counts from a CSV file."),
        ("How would you structure the project files?", "main.py, data.csv, charts/, README.md"),
        ("What is a minimum viable product?", "The simplest version that works end-to-end."),
        ("Write pseudocode for loading data, filtering it, and plotting a chart.", "load CSV; filter rows; calculate counts; plot bar chart; show/save."),
        ("How would you handle bad or missing CSV values?", "Skip rows, use defaults, or report errors."),
        ("What makes a chart in a project trustworthy?", "Clear labels, source citation, and correct data."),
        ("Explain how to add a user menu in a text-based program.", "Print options, accept input, use if/elif to call functions."),
        ("Which testing strategy proves your data pipeline works?", "Test with a small known CSV and compare output."),
        ("How would you document the project for another coder?", "README with setup, file list, and function descriptions."),
        ("Map the mini-project to CBE competencies.", "Data handling, Creativity, Critical Thinking, Communication.")
    ]

    # Week 27: Inputs / physical computing intro
    qb[(27, "10-13")] = [
        ("What is an input on a micro:bit?", "Something the micro:bit can sense, like a button press."),
        ("Name two inputs on a micro:bit.", "Buttons A and B, accelerometer, temperature sensor."),
        ("Which block checks if button A is pressed?", "on button A pressed"),
        ("What does a sensor do?", "It measures something from the environment."),
        ("Write micro:bit code to show a smile when button A is pressed.", "from microbit import *; while True:\n    if button_a.is_pressed():\n        display.show(Image.HAPPY)"),
        ("What is an example of a digital input?", "A button press."),
        ("What is an example of an analog input?", "Temperature or light level."),
        ("Why do mangrove projects need sensors?", "To measure water level, temperature, or soil moisture."),
        ("How do you read the micro:bit temperature?", "temperature()"),
        ("Which CBE strand links to sensors and inputs?", "Computers.")
    ]
    qb[(27, "14-17")] = [
        ("Write micro:bit code that reads button A and sends 'splash' to the serial port.", "from microbit import *\nwhile True:\n    if button_a.was_pressed():\n        print('splash')\n    sleep(100)"),
        ("What is the difference between polling and interrupt-driven input?", "Polling repeatedly checks; interrupts react immediately to an event."),
        ("Explain analog-to-digital conversion in simple terms.", "It turns a continuous measurement like temperature into a digital number."),
        ("How would you debounce a mechanical button in code?", "Wait a short time after detecting a press before checking again."),
        ("Write a function read_button() that returns 'A', 'B', or 'none'.", "def read_button():\n    if button_a.is_pressed(): return 'A'\n    if button_b.is_pressed(): return 'B'\n    return 'none'"),
        ("What is a pull-up resistor used for?", "It keeps an input at a known high state until a button connects it to ground."),
        ("How would you log button presses with timestamps?", "Store (time, button) tuples in a list."),
        ("Name two real sensors used in ocean monitoring.", "Temperature sensor, salinity sensor, pH sensor, turbidity sensor."),
        ("What is sensor calibration?", "Adjusting readings so they match known real values."),
        ("Map inputs to a CBE Computers outcome.", "Learners read data from hardware sensors.")
    ]

    # Week 28: Temperature watch
    qb[(28, "10-13")] = [
        ("Which micro:bit function reads temperature?", "temperature()"),
        ("What unit does the micro:bit temperature sensor use?", "Degrees Celsius."),
        ("Why is coral temperature important?", "Too warm can cause coral bleaching."),
        ("Write code to show 'HOT' if temperature is above 30.", "if temperature() > 30:\n    display.scroll('HOT')"),
        ("What is a threshold?", "A value that triggers an action when crossed."),
        ("If the temperature is 29 and the threshold is 28, what should happen?", "Trigger the warm alert."),
        ("How do you store a temperature reading for later?", "Append it to a list."),
        ("Name one thing you could do if the reef is too warm.", "Show a warning light or send a message."),
        ("Which block category contains comparison operators?", "Operators."),
        ("Which CBE strand links to temperature sensors?", "Computers / Data.")
    ]
    qb[(28, "14-17")] = [
        ("Write a micro:bit program that records temperature every minute and alerts if it exceeds 30°C.", "from microbit import *\nreadings = []\nwhile True:\n    t = temperature()\n    readings.append(t)\n    if t > 30:\n        display.show(Image.SAD)\n    sleep(60000)"),
        ("What is a moving average and why use it with sensor data?", "Average of recent readings; it reduces noise."),
        ("How would you plot temperature readings over time?", "Store (time, temp) pairs and plot temp vs time."),
        ("Explain the difference between accuracy and precision.", "Accuracy is closeness to true value; precision is consistency of repeated readings."),
        ("Write code to compute the average of the last 5 readings.", "avg = sum(readings[-5:]) / len(readings[-5:])"),
        ("What is an actuator? Give an example.", "A device that acts on the world, e.g., a buzzer or LED."),
        ("How would you send an alert without a screen?", "Use a buzzer, radio, or flashing LED."),
        ("Why does coral bleach when water is too warm?", "It loses the algae that give it colour and food."),
        ("Design a threshold with hysteresis: alert above 30, cancel below 27.", "if t > 30: alert = True; elif t < 27: alert = False"),
        ("Map temperature monitoring to CBE outcomes.", "Computers (sensors), Data (logging), Citizenship (conservation).")
    ]

    # Week 29: Tide-guard light / outputs
    qb[(29, "10-13")] = [
        ("What is an output on a micro:bit?", "Something the micro:bit controls, like an LED."),
        ("Which block lights an LED on the micro:bit display?", "display.set_pixel(x, y, 9)"),
        ("How do you turn all LEDs on?", "display.show(Image.HEART)"),
        ("Write code to flash the centre LED three times.", "for _ in range(3):\n    display.set_pixel(2,2,9); sleep(200); display.set_pixel(2,2,0); sleep(200)"),
        ("What colour is a micro:bit LED display?", "Red."),
        ("Why use a light as a tide warning?", "People can see it from far away."),
        ("What does brightness 0 mean?", "Off."),
        ("What does brightness 9 mean?", "Maximum brightness."),
        ("How do you clear the display?", "display.clear()"),
        ("Which CBE strand links to outputs?", "Computers.")
    ]
    qb[(29, "14-17")] = [
        ("Write micro:bit code that pulses an LED pattern when high tide is predicted.", "from microbit import *\ndef tide_warning():\n    for b in range(10):\n        display.set_pixel(2,2,b)\n        sleep(50)\n    display.clear()"),
        ("How do PWM and LED brightness relate?", "PWM varies on-time to control average brightness."),
        ("What is the difference between a digital and analog output?", "Digital is on/off; analog can vary in level."),
        ("Write code to control an external LED on pin 0.", "pin0.write_digital(1)"),
        ("How would you drive a small motor from a micro:bit?", "Use a motor driver board because the micro:bit cannot supply enough current."),
        ("Explain why you need a transistor or relay for high-power outputs.", "Microcontrollers provide low current; transistors/relays switch higher loads."),
        ("What safety concern applies to tide-warning lights near water?", "Waterproofing and electrical isolation."),
        ("Write a function that maps tide height to LED brightness.", "def brightness(height): return min(9, int(height * 2))"),
        ("How would you add sound to a tide warning?", "Attach a buzzer and use pin0.write_analog(frequency)."),
        ("Map outputs to a CBE Computers outcome.", "Learners control hardware actuators based on program logic.")
    ]

    # Week 30: Compass
    qb[(30, "10-13")] = [
        ("Which micro:bit sensor shows direction?", "Compass / magnetometer."),
        ("What does compass.heading() return?", "A direction in degrees from north."),
        ("Which direction is 0 degrees?", "North."),
        ("Which direction is 90 degrees?", "East."),
        ("Write code to show 'N' if pointing north.", "if compass.heading() < 10 or compass.heading() > 350:\n    display.show('N')"),
        ("Why must you calibrate a compass?", "To make the readings accurate."),
        ("What is a heading?", "A direction expressed in degrees."),
        ("Which animal in our lessons uses echolocation and direction?", "Dolphin."),
        ("How can a compass help track an animal?", "It records which direction a tagged animal is moving."),
        ("Which CBE strand links to sensors?", "Computers.")
    ]
    qb[(30, "14-17")] = [
        ("Write micro:bit code that displays an arrow pointing north.", "from microbit import *\nwhile True:\n    display.show(Image.ALL_ARROWS[compass.heading() // 45])"),
        ("How does a digital compass detect direction?", "It measures Earth's magnetic field with a magnetometer."),
        ("What causes compass interference near electronics?", "Metal and magnets can distort the magnetic field."),
        ("Write a function that returns the cardinal direction for a heading.", "def cardinal(h):\n    dirs = ['N','NE','E','SE','S','SW','W','NW']\n    return dirs[int((h + 22.5) % 360 / 45)]"),
        ("How would you log heading data during a dolphin tracking simulation?", "Store (time, heading) tuples in a list."),
        ("What is dead reckoning and why is it hard without GPS?", "Estimating position from direction and distance; errors accumulate."),
        ("Explain how sensor fusion could improve direction tracking.", "Combine compass with accelerometer for tilt compensation."),
        ("Write code to smooth noisy compass readings.", "readings = [compass.heading() for _ in range(5)]; h = sum(readings)/5"),
        ("What is bearing and how does it differ from heading?", "Bearing is direction to a target; heading is direction you face."),
        ("Map compass/direction to CBE Computers and Data outcomes.", "Learners collect and interpret orientation data.")
    ]

    # Week 31: Radio / micro:bit networks
    qb[(31, "10-13")] = [
        ("What does the micro:bit radio do?", "It sends and receives messages between micro:bits."),
        ("Which block turns the radio on?", "radio.on()"),
        ("Which block sends a message?", "radio.send('hello')"),
        ("Write code to send a tag ID when button A is pressed.", "from microbit import *\nimport radio\nradio.on()\nwhile True:\n    if button_a.is_pressed():\n        radio.send('mako-01')"),
        ("What is a network?", "Connected devices that can communicate."),
        ("Why would scientists use radio tags on sharks?", "To track movement without following the animal."),
        ("What could go wrong with a radio message?", "It might not be received, or it could be lost."),
        ("How do two micro:bits know they are on the same network?", "They use the same channel/group."),
        ("What is the range of a micro:bit radio?", "Around 10–20 metres, depending on conditions."),
        ("Which CBE strand links to radio?", "Networks.")
    ]
    qb[(31, "14-17")] = [
        ("Write micro:bit code that receives a radio message and displays it.", "from microbit import *\nimport radio\nradio.on()\nwhile True:\n    msg = radio.receive()\n    if msg:\n        display.scroll(msg)"),
        ("What is a protocol and why is it needed in networking?", "A set of rules so devices understand each other."),
        ("Explain broadcast vs point-to-point communication.", "Broadcast sends to all; point-to-point sends to one specific device."),
        ("How would you add a checksum to a simple tag message?", "Append a simple hash like sum of ASCII values mod 256."),
        ("What is packet loss and how might it affect shark tracking?", "Some messages are not received, causing gaps in the track."),
        ("Write code to set a radio group so two micro:bits can talk privately.", "radio.config(group=7); radio.on()"),
        ("What is latency in a radio network?", "Delay between sending and receiving a message."),
        ("How would you store received tag IDs for later analysis?", "Append them to a list with timestamps."),
        ("Explain the difference between Bluetooth and micro:bit radio.", "Bluetooth pairs devices; micro:bit radio is simpler broadcast."),
        ("Map radio networks to a CBE Networks outcome.", "Learners use simple wireless communication to exchange data.")
    ]

    # Week 32: Simulated shark tracker
    qb[(32, "10-13")] = [
        ("What is a simulation?", "A model of a real thing on a computer."),
        ("Why simulate a shark tracker instead of using a real shark?", "It is safer and cheaper."),
        ("Which data could a simulated shark tracker show?", "Position, time, depth, temperature."),
        ("Write code to move a simulated shark one step east.", "shark_x = shark_x + 1"),
        ("How do you make a tracker update every second?", "Use a loop with sleep(1)."),
        ("What does random.choice([1,-1]) do?", "Picks 1 or -1 randomly."),
        ("Name one thing you could plot from simulated data.", "Shark path on a map."),
        ("Why do simulations use random numbers?", "To model unpredictable movement."),
        ("How do you store a simulated shark position?", "As x and y variables."),
        ("Which CBE strand links simulations?", "Algorithms / Data.")
    ]
    qb[(32, "14-17")] = [
        ("Write Python code that simulates a shark moving randomly in 2D for 50 steps.", "import random\nx, y = 0, 0\nfor _ in range(50):\n    x += random.choice([-1,1])\n    y += random.choice([-1,1])"),
        ("What is a random walk and why is it a simple movement model?", "Each step is random; it approximates movement with no preferred direction."),
        ("How would you add boundaries to a simulation?", "Check if x or y exceeds limits and bounce or clamp."),
        ("Write code to plot a simulated shark path.", "import matplotlib.pyplot as plt; plt.plot(xs, ys); plt.show()"),
        ("What is a seed in a random number generator?", "A starting value that makes randomness reproducible."),
        ("How do you simulate sensor noise?", "Add a small random value to each reading."),
        ("Explain Monte Carlo methods in one sentence.", "Using repeated random sampling to estimate results."),
        ("Write a function that returns distance from shore given x, y coordinates.", "import math; return math.sqrt(x**2 + y**2)"),
        ("How would you validate a simulation against real data?", "Compare statistics like average speed and range."),
        ("Map simulations to CBE Algorithms/Data outcomes.", "Learners model real-world systems using computational methods.")
    ]

    # Week 33: Internet and the ocean
    qb[(33, "10-13")] = [
        ("What is the internet?", "A global network of connected computers."),
        ("What does a web browser do?", "It shows web pages."),
        ("Name two things you can do on the internet.", "Send email, watch videos, research."),
        ("What is a URL?", "The address of a web page."),
        ("Why is the internet useful for ocean research?", "Scientists can share data quickly."),
        ("What is a website?", "A collection of web pages on the internet."),
        ("How can you tell if a website is trustworthy?", "Check the author and source."),
        ("What does 'offline' mean?", "Not connected to the internet."),
        ("Name one Kenyan ocean data source on the internet.", "IFAW, KWS, WCS reports."),
        ("Which CBE strand links to the internet?", "Networks / Digital Literacy.")
    ]
    qb[(33, "14-17")] = [
        ("Explain how DNS translates a domain name to an IP address.", "DNS is like a phone book that maps names to numeric addresses."),
        ("What is HTTP and what does a status code like 404 mean?", "HTTP transfers web data; 404 means the page was not found."),
        ("Write Python code to fetch a webpage's text using requests.", "import requests; r = requests.get('https://example.com'); print(r.text)"),
        ("What is bandwidth and why does it matter in rural Kenya?", "Amount of data that can be sent; limited connectivity affects access."),
        ("How does caching speed up web browsing?", "It stores copies of resources so they load faster next time."),
        ("What is the difference between the internet and the World Wide Web?", "The internet is the network; the Web is a service running on it."),
        ("Explain HTTPS and why it matters.", "HTTPS encrypts data between browser and server, protecting privacy."),
        ("How would you design an offline-first marine data app?", "Store data locally, sync when connected, minimise downloads."),
        ("What is a CDN?", "A network of servers that delivers content from a nearby location."),
        ("Map internet basics to CBE Networks/Digital Literacy outcomes.", "Learners understand how networked systems share information safely.")
    ]

    # Week 34: APIs
    qb[(34, "10-13")] = [
        ("What is an API?", "A way for programs to ask for data from a server."),
        ("What format do many APIs use?", "JSON."),
        ("What does JSON look like?", "Data in curly braces with keys and values."),
        ("Write a request to get an ocean fact API in words.", "Send a GET request to the API URL and read the response."),
        ("Why would a program use an API instead of a webpage?", "An API returns clean data, not a whole page."),
        ("What is a key in JSON?", "The name before a colon."),
        ("What is a value in JSON?", "The data after a colon."),
        ("Name one kind of data an ocean API might give.", "Species facts, tides, weather."),
        ("What happens if the API does not respond?", "Your program should show a friendly error."),
        ("Which CBE strand links to APIs?", "Networks / Data.")
    ]
    qb[(34, "14-17")] = [
        ("Write Python code to fetch JSON from an API and print one field.", "import requests\ndata = requests.get(url).json()\nprint(data['fact'])"),
        ("What is a REST API?", "An API that uses HTTP methods like GET, POST, PUT, DELETE."),
        ("Explain the difference between JSON and XML.", "JSON is lighter and easier to read; XML uses tags."),
        ("How do you handle a failed API request in code?", "Use try/except and check response.status_code."),
        ("What is an API key and why is it private?", "A token that identifies the user; sharing it allows abuse."),
        ("Write code that retries an API call up to 3 times.", "for i in range(3):\n    try:\n        return requests.get(url)\n    except:\n        sleep(1)"),
        ("What is rate limiting?", "A restriction on how many API requests you can make in a time period."),
        ("How would you cache API responses to work offline?", "Save responses to local files and read them if offline."),
        ("What is pagination in an API?", "Returning large results in chunks or pages."),
        ("Map APIs to CBE Networks/Data outcomes.", "Learners retrieve and process remote data programmatically.")
    ]

    # Week 35: Automate tide log
    qb[(35, "10-13")] = [
        ("What does 'automate' mean?", "Make a computer do a task by itself."),
        ("Which Python function writes text to a file?", "file.write()"),
        ("Write code to append a tide height to a file.", "with open('tides.txt', 'a') as f:\n    f.write('1.2\\n')"),
        ("What does 'a' mean in open('log.txt', 'a')?", "Append mode — add to the end without deleting."),
        ("Why is it useful to log data automatically?", "You do not forget and the data is always saved."),
        ("What is a file?", "A saved collection of data on a computer."),
        ("What happens if you open a file in 'w' mode?", "It overwrites the old contents."),
        ("How do you read all lines from a file?", "file.readlines()"),
        ("Name one thing you could log every hour in an ocean project.", "Tide height, temperature, or animal sightings."),
        ("Which CBE strand links to automation?", "Algorithms / Computers.")
    ]
    qb[(35, "14-17")] = [
        ("Write a Python script that appends the current time and tide height to a CSV file.", "import datetime\nwith open('tides.csv','a') as f:\n    f.write(f'{datetime.now().isoformat()},1.2\\n')"),
        ("What is the difference between CSV and JSON file formats?", "CSV is rows of comma-separated values; JSON is structured key-value pairs."),
        ("How would you schedule a Python script to run every hour on Linux?", "Use cron: 0 * * * * python3 script.py"),
        ("Explain file handling context managers and why to use them.", "with open(...) automatically closes the file even if an error occurs."),
        ("Write code that reads a log and counts how many readings exceeded 2 metres.", "with open('tides.txt') as f:\n    count = sum(1 for line in f if float(line.strip()) > 2)"),
        ("What is log rotation?", "Archiving old log files so current logs stay small."),
        ("How do you avoid data loss if a program crashes while writing a file?", "Write to a temporary file, then rename it."),
        ("What is a timestamp and why include it in logs?", "It records exactly when each entry was created."),
        ("How would you parse a CSV log into a list of dictionaries?", "Use csv.DictReader."),
        ("Map file automation to CBE Algorithms/Data outcomes.", "Learners write programs that persist and process data over time.")
    ]

    # Week 36: Physical computing showcase
    qb[(36, "10-13")] = [
        ("What is physical computing?", "Using code to control real-world objects like lights and sensors."),
        ("Name two micro:bit projects from this term.", "Temperature watch, tide-guard light, compass dolphin, radio tag."),
        ("What should you do before demonstrating a hardware project?", "Test all parts."),
        ("How do you explain your micro:bit project to a visitor?", "Say what it does and what problem it solves."),
        ("What is one safety rule for hardware projects?", "Keep water away from electronics."),
        ("Which block sends a radio message?", "radio.send()"),
        ("Name one input and one output in your showcase.", "[Teacher checks: input and output from the student's project]"),
        ("Why is a showcase useful for learning?", "You share ideas and get feedback."),
        ("What is a demo?", "A short live show of how something works."),
        ("Which CBE strand links to showcases?", "Creativity / Communication.")
    ]
    qb[(36, "14-17")] = [
        ("Write a short project pitch for a physical computing showcase.", "My project monitors reef temperature and flashes a warning if it gets too hot, helping protect coral."),
        ("How do you plan a hardware demo to avoid failure?", "Test in the real environment, bring backups, and have a video fallback."),
        ("What is a schematic?", "A diagram of how electronic components connect."),
        ("Explain the difference between firmware and software.", "Firmware runs on hardware devices; software runs on general computers."),
        ("How would you combine sensor input and radio output in one project?", "Read a sensor, decide if an alert is needed, then broadcast a message."),
        ("What is user testing for hardware?", "Watching real users interact with the device and noting problems."),
        ("How do you document a hardware build?", "Photos, wiring diagram, code, and a short README."),
        ("Name two constraints that affect hardware choices in a Kenyan school.", "Cost, power supply, internet access, durability."),
        ("What is a fail-safe and why does it matter for environmental sensors?", "A behaviour that keeps the system safe if something goes wrong."),
        ("Map physical computing showcase to CBE competencies.", "Creativity, Critical Thinking, Communication, Digital Literacy.")
    ]

    # Week 37: Cybersecurity
    qb[(37, "10-13")] = [
        ("What is a password?", "A secret word or phrase that proves who you are."),
        ("Why should passwords be hard to guess?", "So other people cannot access your account."),
        ("Give one example of a strong password.", "A phrase like BlueTurtle$2026!"),
        ("What is phishing?", "A fake message that tries to trick you into giving information."),
        ("How do you know an email might be phishing?", "It asks for passwords or has strange links."),
        ("What should you do if you see a suspicious link?", "Do not click it; tell an adult."),
        ("Why is it important to log out of shared computers?", "So the next person cannot use your account."),
        ("What does 'private' mean online?", "Only you or approved people can see it."),
        ("Name one way to protect a school coding account.", "Use a strong password and do not share it."),
        ("Which CBE strand links to cybersecurity?", "Security.")
    ]
    qb[(37, "14-17")] = [
        ("Write a Python function that rates a password as weak, medium, or strong.", "def rate(pw):\n    score = 0\n    if len(pw) > 8: score += 1\n    if any(c.isupper() for c in pw): score += 1\n    ... return ['weak','medium','strong'][min(score,2)]"),
        ("What is hashing and why are passwords hashed?", "Hashing turns a password into a fixed value; even database leaks do not reveal the password."),
        ("Explain two-factor authentication in simple terms.", "You need two proofs of identity, like a password and a phone code."),
        ("What is a man-in-the-middle attack?", "An attacker secretly intercepts messages between two parties."),
        ("How does HTTPS protect against this?", "It encrypts the connection so attackers cannot read the data."),
        ("Write code to generate a random passphrase of four words.", "import random; words = ['blue','shark','reef','tide']; print(' '.join(random.sample(words,4)))"),
        ("What is social engineering?", "Tricking people into revealing secrets instead of breaking technology."),
        ("How would you secure a classroom micro:bit network?", "Use a private radio group and avoid sending sensitive data."),
        ("What is a firewall used for?", "To block unwanted network traffic."),
        ("Map cybersecurity to a CBE Security outcome.", "Learners apply safe practices to protect digital systems and data.")
    ]

    # Week 38: Digital citizenship
    qb[(38, "10-13")] = [
        ("What is digital citizenship?", "Being safe, kind, and responsible online."),
        ("Give one example of being kind online.", "Writing positive comments."),
        ("What should you do if you see cyberbullying?", "Tell a trusted adult."),
        ("Why should you not copy someone else's project?", "It is their work, not yours."),
        ("What does 'give credit' mean?", "Say who made the original work."),
        ("How can technology help clean coasts?", "Apps can report trash locations."),
        ("What is one way technology can harm nature?", "Spreading false information or sharing secret animal locations."),
        ("Why should you check facts before sharing?", "So you do not spread misinformation."),
        ("What is a digital footprint?", "The record of what you do online."),
        ("Which CBE strand links to digital citizenship?", "Citizenship.")
    ]
    qb[(38, "14-17")] = [
        ("Explain netiquette and give two rules.", "Network etiquette: be respectful, avoid all-caps, credit sources."),
        ("How can open-source software help environmental projects?", "It is free to use, inspect, and improve."),
        ("What is a software license and why does it matter?", "It states how code may be used or shared."),
        ("Write a short acceptable-use policy for a school coding lab.", "Use school devices for learning; do not install unapproved software; respect others' work."),
        ("How do you report harmful content responsibly?", "Use platform reporting tools and tell a trusted adult."),
        ("What is algorithmic bias and why is it a citizenship issue?", "When programs treat groups unfairly; it affects real people's lives."),
        ("How can you verify an ocean conservation claim online?", "Check the source, date, and supporting evidence."),
        ("What is the difference between attribution and plagiarism?", "Attribution gives credit; plagiarism pretends work is your own."),
        ("Explain how technology can amplify community voices.", "Social media and websites let local people share their own stories globally."),
        ("Map digital citizenship to CBE Citizenship/Communication outcomes.", "Learners participate online responsibly and ethically.")
    ]

    # Week 39: Term 3 showcase
    qb[(39, "10-13")] = [
        ("Name one micro:bit or Python project you built this term.", "[Teacher checks: project name]"),
        ("What is one thing you learned about sensors?", "[Teacher checks: sensor concept]"),
        ("How is networking different from writing code on one computer?", "It lets devices talk to each other."),
        ("What is one cybersecurity rule you follow?", "[Teacher checks: rule]"),
        ("What will you improve in your project?", "[Teacher checks: improvement plan]"),
        ("How do you show a project to the class?", "Explain and demonstrate it."),
        ("What feedback did you receive?", "[Teacher checks: feedback]"),
        ("Which Python concept from this term was hardest?", "[Teacher checks: concept]"),
        ("What do you want to build next term?", "[Teacher checks: goal]"),
        ("Which CBE competency did you use most?", "[Teacher checks: competency]")
    ]
    qb[(39, "14-17")] = [
        ("Reflect on one hardware/network project. What worked and what did not?", "[Teacher checks: reflection]"),
        ("How would you explain a network protocol to a beginner?", "A set of rules so devices can talk, like a shared language."),
        ("What is one limitation of micro:bit radio that affects design?", "Short range and possible interference."),
        ("How did you make your project usable for others?", "Clear instructions, simple interface, helpful messages."),
        ("What security or privacy concern did you consider?", "[Teacher checks: concern]"),
        ("How do you measure success for a creative tech project?", "Does it work, is it usable, does it meet the brief?"),
        ("What transferable skill from this term helps outside coding?", "Problem solving, planning, or teamwork."),
        ("How would you pitch your project to a conservation group?", "Explain the problem it solves and show a working demo."),
        ("What documentation did you write?", "[Teacher checks: docs]"),
        ("Which CBE strand was the focus of your showcase?", "[Teacher checks: strand]")
    ]

    # Week 40: Planning capstone
    qb[(40, "10-13")] = [
        ("What is a capstone project?", "A big final project that shows what you learned."),
        ("What will the Mako Shark Expedition project be about?", "A conservation-themed game or dashboard."),
        ("Name three features you could include.", "Player movement, species facts, scoring, charts."),
        ("What is a project plan?", "A list of steps and features to build."),
        ("Why is planning important before coding?", "It saves time and helps the team agree."),
        ("Write one user story for your capstone.", "As a player, I want to move the shark so I can explore the reef."),
        ("What tool will you mainly use for the capstone?", "Python + Pygame Zero."),
        ("Name one ocean species to include.", "Shortfin mako shark."),
        ("What is a milestone?", "A small goal along the way to the final project."),
        ("Which CBE strand links to project planning?", "Project / Communication.")
    ]
    qb[(40, "14-17")] = [
        ("Write a one-page project brief for the Mako Shark Expedition.", "Goal, audience, features, data sources, timeline, and success criteria."),
        ("What is scope creep and how do you avoid it?", "Adding too many features; define MVP and stick to it."),
        ("How would you decompose the capstone into 4 weekly sprints?", "Week 1: world + species; Week 2: interactions; Week 3: data + conservation; Week 4: polish."),
        ("What is a user persona?", "A fictional user that represents your target audience."),
        ("How do you choose between Pygame Zero and a web dashboard for the capstone?", "Pygame Zero is simpler for games; web dashboards are easier to share."),
        ("Write a risk register entry for a capstone project.", "Risk: missing assets. Mitigation: use shapes/text instead of images."),
        ("Explain how to align capstone features with CBE outcomes.", "Each feature should demonstrate a target competency."),
        ("What version control practice helps a team project?", "Regular commits and clear commit messages."),
        ("How do you decide which language/framework to use?", "Based on learner skills, hardware, and project goals."),
        ("Map capstone planning to CBE Project outcomes.", "Learners plan, resource, and manage a complex coding project.")
    ]

    # Week 41: Functions revisited
    qb[(41, "10-13")] = [
        ("What is the purpose of a function?", "To reuse a block of code."),
        ("Write a Python function that draws a mako shark using text.", "def draw_mako():\n    print('\\   \\\n    >\\_\\___)  ')"),
        ("What does def mean in Python?", "It defines a function."),
        ("How do you call a function named swim?", "swim()"),
        ("What is a parameter?", "A value a function needs to work."),
        ("Write a function move_shark(steps) that moves a shark.", "def move_shark(steps):\n    shark_x += steps"),
        ("Why should functions have clear names?", "So others understand what they do."),
        ("What is the difference between a function and a variable?", "A function does something; a variable holds a value."),
        ("How many return statements can a function have?", "Usually one, but it can have more with conditions."),
        ("Which CBE strand links to functions?", "Algorithms.")
    ]
    qb[(41, "14-17")] = [
        ("Write a Python function hunt_mode(is_day, energy) that returns True only during the day with enough energy.", "def hunt_mode(is_day, energy):\n    return is_day and energy > 50"),
        ("What is a pure function?", "A function with no side effects and the same output for the same input."),
        ("Explain the difference between positional and keyword arguments.", "Positional rely on order; keyword are named."),
        ("Write a function with default parameters.", "def greet(name, greeting='Hello'):\n    print(greeting, name)"),
        ("What is function composition?", "Using the output of one function as the input of another."),
        ("How do you test a function with many possible inputs?", "Use a table of test cases or small unit tests."),
        ("Write a recursive function for the Fibonacci sequence.", "def fib(n):\n    return n if n < 2 else fib(n-1) + fib(n-2)"),
        ("What is memoization and why use it?", "Storing results of expensive function calls to avoid recomputation."),
        ("How do docstrings help maintain functions?", "They describe what the function does, its parameters, and return value."),
        ("Map advanced functions to CBE Algorithms outcomes.", "Learners design robust, reusable procedures for complex programs.")
    ]

    # Week 42: Classes / OOP
    qb[(42, "10-13")] = [
        ("What is a class?", "A template for making objects."),
        ("What is an object?", "One specific thing made from a class."),
        ("What is an attribute?", "A piece of data stored in an object."),
        ("What is a method?", "A function that belongs to an object."),
        ("Write a class Coral with attributes colour and size.", "class Coral:\n    def __init__(self, colour, size):\n        self.colour = colour\n        self.size = size"),
        ("How do you make an object from a class?", "c = Coral('pink', 10)"),
        ("What does self mean?", "The object itself."),
        ("Name one thing you could model with a class in the reef.", "Fish, shark, coral, turtle."),
        ("Why are classes useful for games?", "They group data and behaviour together."),
        ("Which CBE strand links to classes?", "Algorithms / Project.")
    ]
    qb[(42, "14-17")] = [
        ("Write a Python class Shark with name, x, y, and a swim() method.", "class Shark:\n    def __init__(self, name, x, y):\n        self.name = name; self.x = x; self.y = y\n    def swim(self):\n        self.x += 1"),
        ("What is encapsulation?", "Keeping data and methods that operate on it together inside a class."),
        ("What is inheritance and how could it model sea life?", "A child class gets attributes from a parent class, e.g., WhaleShark inherits Fish."),
        ("Explain the difference between a class attribute and an instance attribute.", "Class attributes are shared; instance attributes belong to one object."),
        ("Write code to create a list of 5 Coral objects with random colours.", "import random; corals = [Coral(random.choice(['red','blue']), 10) for _ in range(5)]"),
        ("What is polymorphism?", "Different classes responding to the same method call."),
        ("How do you override a method in Python?", "Define a method with the same name in the child class."),
        ("What is __init__ used for?", "It sets up a new object's initial state."),
        ("How would you add collision detection between two objects?", "Check if their rectangles or distance overlap."),
        ("Map classes to CBE Algorithms/Project outcomes.", "Learners use object-oriented design to model complex systems.")
    ]

    # Week 43: Data-driven decisions
    qb[(43, "10-13")] = [
        ("What does 'data-driven' mean?", "Making choices based on data."),
        ("Give one example of using data to protect the ocean.", "Closing a beach if too many turtles are nesting there."),
        ("What is a chart used for?", "To see patterns in data."),
        ("If more plastic is found on Mondays, what could you decide?", "Schedule cleanups on Mondays."),
        ("How do you know if data is trustworthy?", "Check who collected it and how."),
        ("What is a decision?", "Choosing one action from several options."),
        ("Write a rule: if temperature > 30 then alert.", "if temperature > 30: alert()"),
        ("Why is it better to use data than guessing?", "Data helps you make informed choices."),
        ("Name one source of Kenyan ocean data.", "IFAW, KWS, local surveys."),
        ("Which CBE strand links to data-driven decisions?", "Data / Critical Thinking.")
    ]
    qb[(43, "14-17")] = [
        ("Write a Python function that recommends a conservation action based on population trend.", "def action(trend):\n    if trend < -0.1: return 'urgent protection'\n    elif trend < 0: return 'monitor'\n    else: return 'stable'"),
        ("What is a false positive and a false negative in decision systems?", "False positive: alert when nothing is wrong. False negative: miss a real problem."),
        ("How would you visualise a time series of turtle nest counts?", "Line plot with date on x-axis and count on y-axis."),
        ("Explain the difference between correlation and causation.", "Correlation means variables move together; causation means one causes the other."),
        ("Write code to find the month with the highest plastic collection.", "max(collections, key=lambda m: collections[m])"),
        ("What is a dashboard and why is it useful?", "A live display of key metrics; it helps monitor situations quickly."),
        ("How do you handle conflicting data sources?", "Check methodology, recency, and source credibility."),
        ("What is a confidence interval in simple terms?", "A range that likely contains the true value."),
        ("How would you turn data into a recommendation?", "Analyse trends, identify thresholds, and propose an action."),
        ("Map data-driven decisions to CBE Data/Critical Thinking outcomes.", "Learners use evidence to make and justify decisions.")
    ]

    # Week 44: Events and game loop
    qb[(44, "10-13")] = [
        ("What is a game loop?", "Code that runs over and over to update the game."),
        ("Which function in Pygame Zero runs every frame?", "draw() and update()"),
        ("What happens inside a game loop?", "Check input, update positions, draw screen."),
        ("Write pseudocode for a simple game loop.", "while running:\n    handle input\n    move objects\n    draw screen"),
        ("What is a frame?", "One picture shown by the game."),
        ("How do you make a shark move smoothly?", "Update its position a little each frame."),
        ("What event makes the shark turn left?", "Pressing the left arrow key."),
        ("What does FPS mean?", "Frames per second."),
        ("Why should the game loop keep running quickly?", "So the game feels smooth."),
        ("Which CBE strand links to game loops?", "Algorithms.")
    ]
    qb[(44, "14-17")] = [
        ("Write the skeleton of a Pygame Zero game with update() and draw() functions.", "import pgzrun\ndef update(): pass\ndef draw(): screen.fill('black')\npgzrun.go()"),
        ("What is the difference between update() and draw() in a game loop?", "update() changes state; draw() renders the current state."),
        ("How do you keep movement frame-rate independent?", "Multiply speed by delta time."),
        ("Explain collision detection in a 2D game.", "Check if the bounding boxes or circles of two objects overlap."),
        ("Write code to clamp a value between a minimum and maximum.", "x = max(min_x, min(x, max_x))"),
        ("What is a state machine and how does it help game design?", "A model with distinct states like 'menu', 'playing', 'game over'."),
        ("How would you handle multiple key presses at once?", "Track key states in a dictionary or use built-in keyboard properties."),
        ("What is double buffering and why is it used?", "Drawing to an off-screen buffer to prevent flickering."),
        ("Write code to detect when a shark leaves the screen.", "if shark.x < 0 or shark.x > WIDTH: shark.x = WIDTH/2"),
        ("Map game loops to CBE Algorithms outcomes.", "Learners implement real-time interactive programs.")
    ]

    # Week 45: Capstone world & species
    qb[(45, "10-13")] = [
        ("What is the setting of your capstone project?", "The Kenyan coast / ocean."),
        ("Name three species in your capstone world.", "[Teacher checks: species list]"),
        ("How do you create the ocean background in Pygame Zero?", "screen.fill('blue') or blit an image."),
        ("What is a sprite in a game?", "A moving image or shape."),
        ("Write code to draw a circle for a fish.", "screen.draw.filled_circle((x, y), 20, 'orange')"),
        ("How do you place species at different starting positions?", "Use different x, y coordinates."),
        ("Why should your world include real Kenyan species?", "It teaches players about local wildlife."),
        ("What is one piece of data each species could have?", "Speed, size, or conservation status."),
        ("How do you test that your world loads?", "Run the program and check the screen."),
        ("Which CBE strand links to capstone building?", "Project / Creativity.")
    ]
    qb[(45, "14-17")] = [
        ("Write a function load_species() that returns a list of species dictionaries.", "def load_species():\n    return [{'name':'mako','speed':5}, {'name':'turtle','speed':2}]"),
        ("How do you manage game assets without external images?", "Use shapes, colours, text, and emoji-style drawings."),
        ("What is a world file or level file?", "Data that describes the layout and contents of a game world."),
        ("Write code to draw a species at a position from a dictionary.", "s = species[0]; screen.draw.filled_circle((s['x'], s['y']), s['size'], s['colour'])"),
        ("How would you load species data from a JSON file?", "import json; data = json.load(open('species.json'))"),
        ("What is the advantage of separating data from code?", "You can change species without changing the program logic."),
        ("Explain how to handle different screen sizes in a game.", "Use relative positions or scale based on WIDTH/HEIGHT."),
        ("How do you verify that all species appear in the world?", "Add temporary labels or print their positions."),
        ("What is a configuration file and why use one?", "A file that sets options without changing code, e.g., difficulty."),
        ("Map capstone world-building to CBE Project/Data outcomes.", "Learners build a structured, data-backed digital environment.")
    ]

    # Week 46: Capstone interactions
    qb[(46, "10-13")] = [
        ("What is an interaction in a game?", "When the player or objects affect each other."),
        ("Give one example of an interaction in the Mako Shark Expedition.", "Shark eats fish, player collects data, shark hits reef."),
        ("How do you know if two sprites are touching?", "Check if their positions are close."),
        ("Write code to increase score when the shark touches a fish.", "if shark.distance_to(fish) < 30:\n    score += 1"),
        ("What happens when the shark hits a plastic bag?", "Score goes down or health decreases."),
        ("Why are interactions important for gameplay?", "They make the game fun and meaningful."),
        ("Name one sound or effect you could add to an interaction.", "Splash sound or flash effect."),
        ("How do you make an interaction repeatable?", "Reset the object after it is used."),
        ("What is player feedback?", "Signals that tell the player something happened."),
        ("Which CBE strand links to interactions?", "Algorithms / Project.")
    ]
    qb[(46, "14-17")] = [
        ("Write a collision function that checks overlap of two rectangles.", "def collide(a, b):\n    return a.x < b.x + b.w and a.x + a.w > b.x and a.y < b.y + b.h and a.y + a.h > b.y"),
        ("What is the difference between AABB and circle collision detection?", "AABB uses rectangles; circle uses distance from centres."),
        ("How would you implement a scoring system with combos?", "Increase multiplier when multiple quick interactions happen."),
        ("Write code to spawn a new fish after one is collected.", "import random; fish.x = random.randint(50, WIDTH-50); fish.y = random.randint(50, HEIGHT-50)"),
        ("What is a hitbox?", "The invisible shape used for collision checks."),
        ("How do you prevent the same interaction from triggering twice in one frame?", "Use a flag or cooldown timer."),
        ("Explain event-driven vs polling input in Pygame Zero.", "Event-driven reacts to key events; polling checks keyboard state each frame."),
        ("What is game feel and how do interactions create it?", "The satisfying response to player actions, e.g., juice, screenshake."),
        ("How would you log interaction events for later analysis?", "Append events to a list with timestamps."),
        ("Map game interactions to CBE Algorithms/Creativity outcomes.", "Learners design responsive, engaging systems.")
    ]

    # Week 47: Capstone data & conservation
    qb[(47, "10-13")] = [
        ("What conservation message could your capstone share?", "Protect sharks and reefs."),
        ("How can your game show real data?", "Display facts about species when they appear."),
        ("Write a line of code that shows a conservation tip on screen.", "screen.draw.text('Reduce plastic!', (100, 50))"),
        ("What is the IUCN status of the shortfin mako shark?", "Vulnerable."),
        ("Why is it important to show correct facts in your game?", "Players learn from the game."),
        ("Name one human action that harms the ocean.", "Plastic pollution, overfishing."),
        ("How can your project encourage players to help?", "Give them conservation tips or links."),
        ("What is a fact file?", "A small file with true information about a species."),
        ("How do you keep data in your game up to date?", "Read from an external file."),
        ("Which CBE strand links to conservation messaging?", "Citizenship / Project.")
    ]
    qb[(47, "14-17")] = [
        ("Write code that loads a JSON file of conservation facts and displays one randomly.", "import random, json\nfacts = json.load(open('facts.json'))\nscreen.draw.text(random.choice(facts), (50, 50))"),
        ("How would you integrate real survey data into a game without exposing sensitive locations?", "Aggregate by region and remove exact coordinates."),
        ("What is a call-to-action and how do you include one responsibly?", "A prompt asking the player to act, e.g., 'Learn more at KWS' with a real, safe link."),
        ("Explain how your capstone can be both fun and educational.", "Gameplay mechanics reinforce real conservation facts."),
        ("Write a function that updates a conservation score based on player behaviour.", "def update_score(score, collected_plastic):\n    return score + len(collected_plastic) * 10"),
        ("How do you verify the accuracy of facts shown in your project?", "Cross-check with sources like IUCN, KWS, IFAW."),
        ("What is impact design in an educational game?", "Designing so the game produces real learning outcomes."),
        ("How would you localise conservation messages to Kiswahili?", "Store messages in both languages and choose based on user preference."),
        ("What privacy concerns apply if your game collects player scores?", "Do not collect personal identifiers without consent."),
        ("Map conservation data integration to CBE Citizenship/Data outcomes.", "Learners combine evidence with advocacy in digital products.")
    ]

    # Week 48: Capstone polish & evaluate
    qb[(48, "10-13")] = [
        ("What does 'polish' mean in a project?", "Improving details to make it better."),
        ("Name two things you can polish in your capstone.", "Add instructions, fix bugs, improve colours."),
        ("How do you know if your game is fun?", "Ask someone to play it and watch their reaction."),
        ("What is a bug that you fixed this week?", "[Teacher checks: bug]"),
        ("Why is it important to test your game with others?", "They find problems you missed."),
        ("Write one improvement you made.", "[Teacher checks: improvement]"),
        ("What is a final check before sharing?", "Make sure it runs without errors."),
        ("How do you explain your game to a player?", "Tell them the goal and controls."),
        ("Name one thing you are proud of in your capstone.", "[Teacher checks: pride point]"),
        ("Which CBE strand links to evaluation?", "Learning to Learn / Communication.")
    ]
    qb[(48, "14-17")] = [
        ("Write a rubric with three criteria for evaluating your capstone.", "Gameplay, correctness of facts, code quality / usability."),
        ("What is user acceptance testing?", "Testing whether the product meets user needs."),
        ("How do you prioritise bugs before a deadline?", "Fix crashes first, then gameplay, then polish."),
        ("Explain the difference between alpha and beta testing.", "Alpha is internal; beta is with external users."),
        ("Write a short script for observing a player test your game.", "Watch for confusion, count bugs, ask what they learned."),
        ("What is refactoring and why do it?", "Improving code structure without changing behaviour; makes code easier to maintain."),
        ("How do you measure performance in a game?", "Check FPS and memory use."),
        ("What is accessibility and why add it?", "Making the project usable by people with different abilities."),
        ("How would you document known issues in your project?", "Add a TODO or issues list in the README."),
        ("Map evaluation to CBE Learning to Learn/Critical Thinking outcomes.", "Learners assess quality and iterate based on feedback.")
    ]

    # Week 49: UI / accessibility
    qb[(49, "10-13")] = [
        ("What is a user interface?", "The parts of a program that the user sees and uses."),
        ("Give one example of a good UI feature.", "Clear buttons, labels, instructions."),
        ("Why should text be big enough to read?", "So everyone can see it."),
        ("What is accessibility?", "Making sure everyone can use the program."),
        ("Name one way to help someone who cannot see images well.", "Add text descriptions."),
        ("How do you show the score on the screen?", "screen.draw.text('Score: ' + str(score), (10, 10))"),
        ("Why should colours be easy to tell apart?", "Some people cannot see certain colours."),
        ("What is a control?", "A way the user gives input, like a key or button."),
        ("How do you explain the controls to a player?", "Show them on the screen at the start."),
        ("Which CBE strand links to UI/accessibility?", "Digital Literacy / Citizenship.")
    ]
    qb[(49, "14-17")] = [
        ("Write code that draws a UI panel showing score, level, and health.", "screen.draw.filled_rect(Rect(0,0,200,60), 'black')\nscreen.draw.text(f'Score: {score}', (10, 10))"),
        ("What are WCAG and why do they matter?", "Web Content Accessibility Guidelines; they help make content usable for all."),
        ("How would you make a game playable with only a keyboard?", "Ensure all actions have keyboard controls and visible focus."),
        ("Explain colour contrast and why it matters.", "Sufficient contrast makes text readable for people with low vision."),
        ("What is alt text and when do you use it?", "Text description of an image; used when images cannot be seen."),
        ("How do you test accessibility without specialised tools?", "Try using only keyboard, increase font size, or use a screen reader."),
        ("Write a function that scales UI elements based on screen size.", "def ui_scale(base): return base * WIDTH / 800"),
        ("What is inclusive design?", "Designing products that work for the widest range of people."),
        ("How would you add subtitles or captions to a game?", "Display text when sounds play or speech occurs."),
        ("Map UI/accessibility to CBE Digital Literacy/Citizenship outcomes.", "Learners design inclusive digital interfaces.")
    ]

    # Week 50: Peer review
    qb[(50, "10-13")] = [
        ("What is peer review?", "When classmates look at each other's work and give feedback."),
        ("What is one kind thing to say in a review?", "I like how you..."),
        ("What is one helpful suggestion to give?", "You could add..."),
        ("Why should you be kind when reviewing?", "It helps the other person learn."),
        ("What is a beta test?", "Letting others try your project before the final version."),
        ("How do you record feedback?", "Write it down."),
        ("Name one thing to check when testing a classmate's game.", "Does it start? Are the controls clear?"),
        ("What should you do with feedback?", "Use it to improve your project."),
        ("How do you respond to feedback?", "Listen, ask questions, and decide what to change."),
        ("Which CBE strand links to peer review?", "Communication / Collaboration.")
    ]
    qb[(50, "14-17")] = [
        ("Write a peer review checklist for the Mako Shark Expedition.", "Runs without errors, clear controls, accurate facts, fun, conservation message."),
        ("What is constructive criticism?", "Feedback that points out problems and suggests improvements."),
        ("How do you avoid bias when reviewing a friend's project?", "Use the same checklist for everyone."),
        ("What is a bug report and what should it include?", "Steps to reproduce, expected behaviour, actual behaviour, environment."),
        ("Explain how to triage issues found in beta testing.", "Sort by severity: crashes first, then usability, then polish."),
        ("How do you give feedback on code quality?", "Comment on readability, organisation, and whether functions are clear."),
        ("What is a code review and why is it important?", "A peer checks code for errors and improvements; it catches bugs early."),
        ("How would you run a structured playtest session?", "Define tasks, observe players, record issues, debrief."),
        ("What is a retrospective in a team?", "A meeting to discuss what went well and what to improve."),
        ("Map peer review to CBE Communication/Collaboration outcomes.", "Learners give and act on structured feedback.")
    ]

    # Week 51: Final presentation rehearsal
    qb[(51, "10-13")] = [
        ("What should you include in a presentation?", "What you built, how it works, and why it matters."),
        ("How long should your presentation be?", "About 2–5 minutes."),
        ("What is one way to practice a presentation?", "Rehearse in front of a mirror or friend."),
        ("Why should you speak slowly?", "So people can understand you."),
        ("What is a demo?", "Showing the project working live."),
        ("How do you answer a question you do not know?", "Say you are not sure but will find out."),
        ("Name two things to check before presenting.", "Project works, slides are ready, notes are brief."),
        ("What do you do if the program crashes during a demo?", "Stay calm and explain what you planned to show."),
        ("Why is eye contact important when presenting?", "It connects you with the audience."),
        ("Which CBE strand links to presentations?", "Communication.")
    ]
    qb[(51, "14-17")] = [
        ("Write an outline for a 5-minute capstone presentation.", "Hook, problem, solution/demo, technical highlights, impact, Q&A."),
        ("What is a backup plan for a live demo?", "Have screenshots or a short video ready."),
        ("How do you tailor a presentation to different audiences?", "Use different examples and depth based on who is listening."),
        ("Explain the rule of three in presentations.", "People remember ideas better in groups of three."),
        ("How do you handle nerves before presenting?", "Practice, breathe, and focus on the message."),
        ("What is a call-to-action in a final presentation?", "A clear request, e.g., 'Try the game and share one ocean fact.'"),
        ("How do you use slides without reading from them?", "Put keywords on slides and speak from notes."),
        ("What questions should you expect from judges?", "Why this project, how it works, what you learned, next steps."),
        ("How would you present code without overwhelming the audience?", "Show one key function and explain it in plain language."),
        ("Map presentation skills to CBE Communication outcomes.", "Learners communicate ideas clearly and confidently.")
    ]

    # Week 52: Capstone showcase
    qb[(52, "10-13")] = [
        ("What is the final project called?", "Mako Shark Expedition."),
        ("Name one thing your project teaches about the ocean.", "[Teacher checks: conservation or species fact]"),
        ("What did you enjoy most while building it?", "[Teacher checks: student reflection]"),
        ("What is one skill you improved?", "[Teacher checks: coding or soft skill]"),
        ("How does your project help ocean conservation?", "[Teacher checks: awareness/action]"),
        ("What is one piece of feedback you used?", "[Teacher checks: feedback applied]"),
        ("Name one coding concept you used in the project.", "Loops, variables, functions, classes."),
        ("What would you add if you had more time?", "[Teacher checks: future improvement]"),
        ("How did you work with classmates?", "[Teacher checks: collaboration]"),
        ("Which CBE strand is most important in the showcase?", "Citizenship / Communication / Project.")
    ]
    qb[(52, "14-17")] = [
        ("Write a one-paragraph reflection on completing the Mako Shark Expedition.", "[Teacher checks: reflection]"),
        ("How would you continue the project after the course ends?", "Add more species, real data, or publish it."),
        ("What is the social impact of your capstone?", "It raises awareness of Kenyan marine conservation."),
        ("How do you measure whether the project met its learning goals?", "Compare features to the brief and assess feedback."),
        ("Explain one trade-off you made during development.", "[Teacher checks: trade-off]"),
        ("What would you do differently in a future team project?", "[Teacher checks: improvement]"),
        ("How does open-source sharing align with conservation goals?", "It lets others build on and spread the work."),
        ("What is your strongest technical achievement?", "[Teacher checks: achievement]"),
        ("How do you plan to keep learning coding after this course?", "[Teacher checks: plan]"),
        ("Map the capstone showcase to overall CBE outcomes.", "Learners integrate competencies to create and share a meaningful digital solution.")
    ]

    return qb


def write_quiz(week: int, slug: str, title: str, age_band: str, items: list[tuple[str, str]]):
    age_label = "Ages 10–13" if age_band == "10-13" else "Ages 14–17"
    lines = [
        f"# Week {week:02d} Quiz — {title} — {age_label}",
        "",
        f"> *10 code-focused, CBE-aligned questions for Week {week:02d}: {title}.*",
        "",
        "## Questions",
        "",
    ]
    for i, (q, a) in enumerate(items, 1):
        lines.append(f"{i}. {q}")
    lines.extend([
        "",
        "## Answer Key",
        "",
    ])
    for i, (q, a) in enumerate(items, 1):
        lines.append(f"{i}. {a}")
    lines.append("")
    path = QUIZZES_DIR / f"quiz-{week:02d}-{slug}-{age_band}.md"
    path.write_text("\n".join(lines), encoding='utf-8')


def main():
    qb = question_bank()
    for number, slug, title, *_ in MODULES:
        write_quiz(number, slug, title, "10-13", qb[(number, "10-13")])
        write_quiz(number, slug, title, "14-17", qb[(number, "14-17")])
    print(f"Rewrote {len(MODULES) * 2} quiz files.")


if __name__ == "__main__":
    main()
