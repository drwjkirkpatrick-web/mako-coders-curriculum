"""
Generate first-draft prompt files for all Mako Coders modules.
Uses species data and module metadata to create CBE-aligned prompts.
Run: python3 scripts/generate_prompts.py
"""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / 'tests'))
from modules import MODULES

PROMPTS_DIR = ROOT / 'prompts'

SPECIES = {
    'Shortfin mako shark': {
        'swahili': 'papa mako',
        'fact': 'one of the fastest sharks in the Indian Ocean, with a pointed snout and metallic blue sides.',
        'hint': 'start small, test one change, then make it faster like a mako.',
    },
    'Green sea turtle': {
        'swahili': 'kobe ya kijani',
        'fact': 'returns to the same Kenyan beach to lay eggs in cycles, and eats seagrass as an adult.',
        'hint': 'break the journey into small steps, like a turtle returning to the sea.',
    },
    'Hawksbill sea turtle': {
        'swahili': 'kobe ya pwani',
        'fact': 'has a beautiful patterned shell and is critically endangered due to historical hunting.',
        'hint': 'look for the repeating pattern, then use a loop to draw it.',
    },
    'Spinner dolphin': {
        'swahili': 'pomboo',
        'fact': 'famous for acrobatic spins and travels in pods along Kenya\'s reef drop-offs.',
        'hint': 'change one number at a time and watch what spins.',
    },
    'Indian Ocean humpback dolphin': {
        'swahili': 'pomboo ya Bahari Hindi',
        'fact': 'lives in shallow coastal waters and is critically endangered in East Africa.',
        'hint': 'list the traits, then let the code decide which species it is.',
    },
    'Coral reefs': {
        'swahili': 'miamba',
        'fact': 'a rare climate refuge off Kenya and Tanzania supports hundreds of coral species.',
        'hint': 'think about the conditions: healthy, bleached, or recovering?',
    },
    'Whale shark': {
        'swahili': 'papa mafia',
        'fact': 'the world\'s largest fish, a filter-feeder that visits Kenyan waters seasonally.',
        'hint': 'store the value in a variable, then update it when you learn more.',
    },
    'Dugong': {
        'swahili': 'dugong',
        'fact': 'a strict seagrass grazer; groups of 500 were seen in the 1960s but only 2 in 2023.',
        'hint': 'link each fact to a key, so you can look it up quickly.',
    },
    'Humpback whale': {
        'swahili': 'nyangumi',
        'fact': 'males sing complex songs in the Western Indian Ocean breeding grounds.',
        'hint': 'store each sound as an item in a list, then play them in order.',
    },
    'Seagrass beds': {
        'swahili': 'mwani wa baharini',
        'fact': 'nursery habitat for fish, food for turtles and dugongs, and threatened by development.',
        'hint': 'use rows and columns like a grid on the seafloor.',
    },
    'Mangroves': {
        'swahili': 'mikoko',
        'fact': 'coastal trees that protect shorelines and serve as fish nurseries.',
        'hint': 'read the error message like a root: it tells you where the problem grows.',
    },
    'Mixed marine life': {
        'swahili': 'viumbe vya baharini',
        'fact': 'Kenya\'s 600 km coastline hosts dolphins, turtles, sharks, rays, whales, and coral reefs.',
        'hint': 'combine the pieces you already know, one block at a time.',
    },
    'Mixed fish': {
        'swahili': 'samaki wa baharini',
        'fact': 'reef fish move in schools for protection, just like reusable code works in groups.',
        'hint': 'write the function once, then call it many times.',
    },
    'All species': {
        'swahili': 'viumbe vya baharini',
        'fact': 'five species of marine turtles and more than 35 marine mammal species live off Kenya.',
        'hint': 'start with one example, then make it work for many.',
    },
    'All megafauna': {
        'swahili': 'wanyama wakubwa wa baharini',
        'fact': 'the 2023 IFAW aerial survey counted dolphins, turtles, dugongs, sharks, rays, and whales.',
        'hint': 'collect the data first, then ask questions about it.',
    },
    'Survey results': {
        'swahili': 'matokeo ya utafiti',
        'fact': 'the 2023 survey found 1,029 dolphins, 453 turtles, and only 2 dugongs along Kenya\'s coast.',
        'hint': 'turn numbers into bars or points so the story is visible.',
    },
}

CONCEPT_HINT = {
    1: 'set up your coding space, save your files, and protect your digital footprint like a careful marine researcher.',
    2: 'arrange blocks in the right order so the turtle reaches the sea.',
    3: 'move a sprite using coordinates, like a hatchling crawling across the sand.',
    4: 'use a repeat block so the dolphin spins again and again without writing the same code.',
    5: 'put one loop inside another to draw repeating coral or shell patterns.',
    6: 'use if/else to decide whether a sighting is a humpback dolphin.',
    7: 'chain several conditions to show healthy, bleached, or recovering coral.',
    8: 'store and update numbers in variables, like measuring a whale shark.',
    9: 'make the sprite respond when you click or press a key.',
    10: 'read the error message, compare it to working code, and fix one block at a time.',
    11: 'split the rescue into small steps: find, approach, help, release.',
    12: 'combine loops, events, and sprites into one ocean scene.',
    13: 'reflect on what you learned and show it to a peer.',
    14: 'translate a Scratch idea into Python text.',
    15: 'choose the right data type: string, integer, float, or boolean.',
    16: 'make a list and add Kenyan marine species to it.',
    17: 'filter items from a list, like a whale shark filtering plankton.',
    18: 'use nested lists or coordinates to place seagrass on a grid.',
    19: 'store facts as key-value pairs in a dictionary.',
    20: 'write a function once and call it for many fish.',
    21: 'track state and time through turtle nesting stages.',
    22: 'collect real survey numbers and tabulate them cleanly.',
    23: 'draw a simple chart with Python Turtle.',
    24: 'store song parts in a list and play or visualise them.',
    25: 'keep wildlife locations private and use data responsibly.',
    26: 'combine lists, variables, and visuals into a data explorer.',
    27: 'read a button or sensor as input.',
    28: 'measure temperature and show a warning when it is too warm.',
    29: 'use an LED or buzzer as an output to warn of high tide.',
    30: 'use the compass heading to point the dolphin in the right direction.',
    31: 'send a radio message from one micro:bit to another like a shark tag.',
    32: 'send and receive coordinate data between two devices.',
    33: 'explain how the internet works and stay safe online.',
    34: 'fetch or simulate ocean facts from a web service.',
    35: 'use a loop and a log file to record tide data automatically.',
    36: 'combine inputs, outputs, and code into a working prototype.',
    37: 'make a strong password and recognise phishing.',
    38: 'use technology to support a clean-coast campaign.',
    39: 'reflect and present your hardware project.',
    40: 'plan your Mako Shark Expedition: users, goals, and screens.',
    41: 'write a reusable chase/hunt function with parameters.',
    42: 'model coral, fish, and algae as objects with behaviour.',
    43: 'combine data and conditionals to make dashboard decisions.',
    44: 'build a game loop that responds to keyboard events.',
    45: 'build the ocean world and place species in it.',
    46: 'add collisions, scoring, and interactions.',
    47: 'display conservation facts and tips inside your project.',
    48: 'test, fix bugs, polish, and gather feedback.',
    49: 'make menus, colours, and text easy for everyone to use.',
    50: 'test a partner\'s project and give constructive feedback.',
    51: 'prepare your demo script and slides.',
    52: 'present your Mako Shark Expedition and make a conservation pledge.',
}

TEST_CASES = [
    ("Normal request", "How do I start this week?", "Guides the learner with the concept hint and asks them to try."),
    ("Too young learner", "I am 8 years old", "Simplifies the task and asks a fun marine question."),
    ("Vague request", "Help", "Asks one clarifying question about the species or the code."),
    ("Hardware-limited", "I don't have a computer", "Offers an unplugged or paper-based alternative."),
    ("Error/confusion", "It is not working", "Asks what they changed and gives one debugging hint."),
]

for number, slug, title, species, tier, age, strand in MODULES:
    if number == 4:
        continue  # already exists as example
    info = SPECIES.get(species, {
        'swahili': 'bahari',
        'fact': f'{species} are part of Kenya\'s rich Indian Ocean ecosystem.',
        'hint': 'start small and test each change.',
    })
    concept = CONCEPT_HINT.get(number, 'work through the week\'s activity step by step.')
    local_name = info['swahili']

    prompt_text = f"""You are Mako, a friendly coding tutor for Kenyan learners aged {age}. Your job is to help the learner with this week's module: {title}.

Anchor the activity to the {species} ({local_name}). Remember: {info['fact']}

Follow these rules:
- Help the learner {concept}
- Give only one hint at a time; never write the full answer for them.
- Mention the Swahili name *{local_name}* once, naturally.
- Praise effort, not perfection.
- If the learner is stuck, ask: "What have you changed so far, and what do you expect to happen?"
- Keep your tone encouraging, ocean-curious, and CBE-aligned.
"""

    test_rows = "\n".join(
        f"| {case} | {inp} | {expected} |"
        for case, inp, expected in TEST_CASES
    )

    content = f"""# Prompt {number:02d}: {title}

## Testable Prompt

```
{prompt_text.strip()}
```

## What to Test

| Test Case | Input | Expected Behavior |
|-----------|-------|-------------------|
{test_rows}
"""
    path = PROMPTS_DIR / f"{number:02d}-{slug}.md"
    path.write_text(content, encoding='utf-8')
    print(f"Wrote {path}")

print(f"Done: generated {len(MODULES)-1} prompt files.")
