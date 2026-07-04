"""
Generate first-draft lesson plan files for all Mako Coders modules.
Uses species data and module metadata to create CBE-aligned lesson plans.
Run: python3 scripts/generate_lessons.py
"""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / 'tests'))
from modules import MODULES

LESSONS_DIR = ROOT / 'lessons'

SPECIES = {
    'Shortfin mako shark': {
        'swahili': 'papa mako',
        'habitat': 'tropical and temperate Indian Ocean waters; juveniles near coast, adults offshore',
        'conservation': 'vulnerable globally; often taken as bycatch and targeted catch.',
    },
    'Green sea turtle': {
        'swahili': 'kobe ya kijani',
        'habitat': 'seagrass beds and nesting beaches along the Kenyan coast',
        'conservation': 'endangered; nesting beaches need darkness, quiet, and protection from plastic.',
    },
    'Hawksbill sea turtle': {
        'swahili': 'kobe ya pwani',
        'habitat': 'coral reefs where it eats sponges and soft corals',
        'conservation': 'critically endangered; protected by international law after historical shell trade.',
    },
    'Spinner dolphin': {
        'swahili': 'pomboo',
        'habitat': 'pelagic and coastal Western Indian Ocean waters near reef drop-offs',
        'conservation': 'boat noise and tourism harassment can disrupt resting pods.',
    },
    'Indian Ocean humpback dolphin': {
        'swahili': 'pomboo ya Bahari Hindi',
        'habitat': 'shallow coastal waters, river mouths, and mangrove edges',
        'conservation': 'critically endangered in East Africa; threatened by gillnets and coastal development.',
    },
    'Coral reefs': {
        'swahili': 'miamba',
        'habitat': 'warm shallow seas; a climate refuge exists off Kenya and Tanzania',
        'conservation': 'threatened by bleaching, destructive fishing, and coastal development.',
    },
    'Whale shark': {
        'swahili': 'papa mafia',
        'habitat': 'coastal and offshore; seasonal visitor to Kenyan waters',
        'conservation': 'endangered; boat strikes and irresponsible tourism are major threats.',
    },
    'Dugong': {
        'swahili': 'dugong',
        'habitat': 'seagrass beds in shallow coastal waters',
        'conservation': 'critically endangered; only 2 individuals seen in the 2023 Kenyan aerial survey.',
    },
    'Humpback whale': {
        'swahili': 'nyangumi',
        'habitat': 'breeding grounds in the Western Indian Ocean',
        'conservation': 'recovering globally but threatened by ship strikes and ocean noise.',
    },
    'Seagrass beds': {
        'swahili': 'mwani wa baharini',
        'habitat': 'shallow coastal seabed; nursery for fish and food for turtles/dugongs',
        'conservation': 'threatened by salt pans, shrimp farms, sand mining, and siltation.',
    },
    'Mangroves': {
        'swahili': 'mikoko',
        'habitat': 'intertidal coastal forests and estuaries',
        'conservation': 'overharvested for charcoal and firewood; restoration protects coasts and fisheries.',
    },
    'Mixed marine life': {
        'swahili': 'viumbe vya baharini',
        'habitat': 'Kenya\'s 600 km Indian Ocean coastline',
        'conservation': 'marine ecosystems support 2.7 million people; need community-led protection.',
    },
    'Mixed fish': {
        'swahili': 'samaki wa baharini',
        'habitat': 'coral reefs and seagrass beds',
        'conservation': 'fish stocks depend on healthy habitats and sustainable fishing.',
    },
    'All species': {
        'swahili': 'viumbe vya baharini',
        'habitat': 'Kenyan coastal and marine ecosystems',
        'conservation': 'all marine life benefits from protected areas, clean coasts, and responsible fishing.',
    },
    'All megafauna': {
        'swahili': 'wanyama wakubwa wa baharini',
        'habitat': 'Kenyan territorial waters and pelagic Indian Ocean',
        'conservation': 'large marine animals need monitoring, law enforcement, and habitat protection.',
    },
    'Survey results': {
        'swahili': 'matokeo ya utafiti',
        'habitat': 'data from the 2023 aerial megafauna survey along Kenya\'s coast',
        'conservation': 'survey data guides conservation action and marine protected area planning.',
    },
}

SUBSTRAND = {
    'Algorithms': 'Algorithms and Programming',
    'Data': 'Data and Information',
    'Computers': 'Computers and Hardware',
    'Networks': 'Networks and Communications',
    'Security': 'Cybersecurity and Ethics',
    'Project': 'Project Development',
    'Digital Literacy': 'Digital Literacy and Safety',
    'Critical Thinking': 'Problem Solving and Debugging',
    'Creativity': 'Creative Computing',
    'Learning to Learn': 'Reflection and Portfolio',
    'Communication': 'Communication and Collaboration',
    'Citizenship': 'Digital Citizenship and Conservation',
}

CONCEPT = {
    1: ('digital footprint, safe setup, file organisation, and using computers responsibly', 'Scratch 3', 'folders, rules poster'),
    2: ('sequencing instructions in order', 'Scratch 3', 'ordered movement script'),
    3: ('sprites, motion blocks, and coordinates', 'Scratch 3', 'hatchling reaches the sea'),
    4: ('repeat loops for repetition', 'Scratch 3', 'spinning dolphin animation'),
    5: ('nested loops to make patterns', 'Scratch 3', 'coral or shell pattern'),
    6: ('if/else conditional decisions', 'Scratch 3', 'species ID sprite'),
    7: ('multiple conditions and branching', 'Scratch 3', 'coral health checker'),
    8: ('variables to store and update data', 'Scratch 3', 'whale shark measurement tracker'),
    9: ('events such as key press and green flag', 'Scratch 3', 'interactive dolphin pod'),
    10: ('reading error messages and fixing bugs step by step', 'Scratch 3', 'working mangrove animation'),
    11: ('decomposing a big task into smaller parts', 'Scratch 3 / paper', 'turtle rescue flowchart'),
    12: ('combining skills into a mini-project', 'Scratch 3', 'animated ocean scene'),
    13: ('portfolio reflection and peer presentation', 'Scratch 3', 'portfolio entry'),
    14: ('transition from Scratch blocks to Python text', 'Python + Turtle', 'first Python drawing'),
    15: ('strings, integers, floats, and booleans', 'Python', 'species fact card'),
    16: ('creating and indexing lists', 'Python', 'marine species list'),
    17: ('filtering and operating on lists', 'Python', 'filtered diet list'),
    18: ('nested lists and coordinates', 'Python + Turtle', 'seagrass grid map'),
    19: ('dictionaries as key-value stores', 'Python', 'dugong fact dictionary'),
    20: ('defining and calling functions', 'Python + Turtle', 'reusable fish-school function'),
    21: ('state tracking and timers', 'Python', 'turtle nesting stage timer'),
    22: ('collecting and tabulating real data', 'Python / spreadsheet', 'survey data table'),
    23: ('drawing simple charts', 'Python + Turtle', 'coastal bar chart'),
    24: ('arrays/lists of sound or note data', 'Python + simple audio', 'whale song list'),
    25: ('privacy, location safety, and responsible data use', 'Discussion + Python', 'safe-data pledge'),
    26: ('integrating data, visuals, and interaction', 'Python', 'marine data explorer'),
    27: ('buttons and sensor inputs', 'micro:bit / simulator', 'button dolphin click'),
    28: ('temperature thresholds and alerts', 'micro:bit / simulator', 'temperature warning'),
    29: ('LED and buzzer outputs', 'micro:bit / simulator', 'tide-guard light'),
    30: ('compass heading and angles', 'micro:bit / simulator', 'compass dolphin'),
    31: ('radio messages between devices', 'micro:bit / simulator', 'shark tag message'),
    32: ('sending and receiving coordinate data', 'micro:bit / simulator', 'two-device tracker'),
    33: ('how the internet works and safe research', 'Browser + discussion', 'safe-research checklist'),
    34: ('APIs and JSON data (offline-safe mock)', 'Python', 'offline ocean-fact fetcher'),
    35: ('automation with loops and file logging', 'Python', 'daily tide log'),
    36: ('combining hardware inputs/outputs in a prototype', 'micro:bit / simulator', 'working tide-guard station'),
    37: ('passwords, phishing, and personal safety', 'Discussion + Python', 'secure researcher profile'),
    38: ('using technology for environmental good', 'Discussion + project plan', 'clean-coast campaign'),
    39: ('reflection and presentation of hardware work', 'micro:bit / simulator', 'portfolio update'),
    40: ('planning a capstone project', 'Python / Pygame Zero', 'Mako Shark Expedition design doc'),
    41: ('functions with parameters and return values', 'Python', 'reusable hunt/chase function'),
    42: ('classes and objects for an ecosystem model', 'Python', 'coral reef objects'),
    43: ('combining data and conditionals for decisions', 'Python', 'dashboard data panel'),
    44: ('game loop and keyboard events', 'Python + Pygame Zero', 'keyboard-controlled mako'),
    45: ('building the capstone world and species', 'Python + Pygame Zero', 'playable ocean map'),
    46: ('collisions, scoring, and interactions', 'Python + Pygame Zero', 'hunt/eat/collect mechanic'),
    47: ('displaying conservation facts and tips', 'Python + Pygame Zero', 'educational pop-ups'),
    48: ('testing, bug fixing, and polishing', 'Python + Pygame Zero', 'refined MVP'),
    49: ('user interface and accessibility', 'Python + Pygame Zero / web', 'accessible dashboard'),
    50: ('peer testing and constructive feedback', 'Python + Pygame Zero', 'bug list + fixes'),
    51: ('presentation rehearsal and demo script', 'Any tool', 'rehearsed presentation'),
    52: ('final showcase and conservation pledge', 'Any tool', 'Mako Shark Expedition demo'),
}

LEARNING_OUTCOMES = {
    'Algorithms': ('explain the sequence of instructions', 'apply control structures to solve a problem', 'value clear, ordered thinking in code'),
    'Data': ('explain how data is stored and structured', 'apply data structures to model marine information', 'value data as a tool for conservation'),
    'Computers': ('explain how input and output devices work', 'apply sensor/output code to a micro:bit project', 'value hardware as a way to monitor the ocean'),
    'Networks': ('explain how devices share data', 'apply simple networking code to send/receive messages', 'value connected devices for marine research'),
    'Security': ('explain why online safety and privacy matter', 'apply safe password and data practices', 'value responsible digital behaviour'),
    'Project': ('explain the project development cycle', 'apply design-code-create-connect-evaluate to a capstone', 'value creating technology with a conservation purpose'),
    'Digital Literacy': ('explain safe and effective computer use', 'apply file, editor, and internet skills', 'value digital tools for learning'),
    'Critical Thinking': ('explain how to find and fix errors', 'apply debugging strategies to broken code', 'value persistence when solving problems'),
    'Creativity': ('explain how code can express ideas', 'apply design choices to an original project', 'value creative computing'),
    'Learning to Learn': ('explain what they learned this term', 'apply reflection to improve future work', 'value continuous learning'),
    'Communication': ('explain their project clearly', 'apply feedback to improve their work', 'value collaboration with peers'),
    'Citizenship': ('explain how technology affects communities and nature', 'apply ethical choices about data and conservation', 'value using code for the common good'),
}

for number, slug, title, species, tier, age, strand in MODULES:
    if number == 4:
        continue  # example already exists
    info = SPECIES.get(species, {
        'swahili': 'bahari',
        'habitat': 'Kenyan Indian Ocean waters',
        'conservation': 'marine ecosystems need protection and responsible use.',
    })
    concept, tool, deliverable = CONCEPT.get(number, ('coding concept', 'Scratch 3', 'working artifact'))
    lo1, lo2, lo3 = LEARNING_OUTCOMES.get(strand, LEARNING_OUTCOMES['Algorithms'])
    sub = SUBSTRAND.get(strand, strand)
    local_name = info['swahili']

    content = f"""# Lesson {number:02d}: {title}

- **Module Reference:** Prompt {number:02d}
- **Duration:** 2 hours (10-minute break after guided practice)
- **Age Group:** CBE Junior/Senior School ({age} years)
- **Coding Tool:** {tool}

## CBE Strand Mapping

| CBE Learning Area | Strand | Sub-strand |
|-------------------|--------|------------|
| Computer Studies / ICT | {strand} | {sub} |

## Learning Outcomes

By the end of the lesson the learner should be able to:
1. **Explain** {lo1}.
2. **Apply** {lo2}.
3. **Value** {lo3}.

## Key Inquiry Question

*How can the {species} ({local_name}) help us learn about {concept}?*

## Resources

- {tool} installed on learner devices (offline setup where possible)
- Projector for live demo
- Starter files or handouts as needed
- Reference material from `research/domain-reference.md`

## Local Context: {species}

- **Common name:** {species}
- **Swahili name:** {local_name}
- **Habitat:** {info['habitat']}
- **Why this species:** This species anchors the week's concept because its behaviour or status connects naturally to {concept}.
- **Conservation note:** {info['conservation']}

## Lesson Development

### Intro hook (10 min)
Share a quick fact about the {species} ({local_name}). Ask a question that links the species to the coding concept: "How can we use code to {deliverable.split()[0]}...?"

### Step 1 — Concept + teacher demo (20 min)
Teach the week's concept ({concept}) using a short live demo in {tool}. Connect every block or line of code back to the {species}.

### Step 2 — Guided practice (30 min)
Learners follow along with a starter activity. They make small changes and test frequently. The teacher circulates and uses the anchor species as a memory hook.

### Break (10 min)

### Step 3 — Independent practice (35 min)
Create the main deliverable: **{deliverable}**. Checklist:
- [ ] Core concept from the lesson is present
- [ ] Anchor species ({species}) is referenced in the project
- [ ] Code runs without critical errors
- [ ] One conservation message or note is included

### Step 4 — Sharing and feedback (15 min)
Two or three learners demo their work. Peers give one "glow" (what worked well) and one "grow" (one idea to improve) using CBE rubric language.

## Assessment

| Criterion | BE (0–39%) | AE (40–59%) | ME (60–79%) | EE (80–100%) |
|-----------|------------|-------------|---------------|----------------|
| Understands the concept | Needs help to identify the concept | Identifies the concept with prompting | Explains the concept in own words | Explains and teaches the concept to a peer |
| Completes the main task | Cannot run starter code | Makes 1–2 guided changes | Completes the deliverable with testing | Extends the deliverable with an original feature |
| Conservation connection | No species link | Mentions species but no message | Includes a relevant conservation note | Connects conservation note to the code purpose |

## Extended Activity

Research one additional fact about the {species} and add it to the project. Alternatively, modify the code to respond to a second input or display extra data.

## Differentiation

| Support | Advanced |
|---------|----------|
| Pair with a peer; provide printed block/code cards; reduce the number of required features. | Add a second species, create a reusable block/function, or add user-controlled parameters. |

## Teacher Reflection

- [ ] Did every learner successfully run or build something today?
- [ ] Did I use the anchor species ({species}) to make the concept memorable?
- [ ] Did I give wait-time before answering questions?
- [ ] Did learners use CBE language during sharing?
- [ ] What will I re-teach or extend next week?

## RPF & CBE Cross-Reference

| RPF Strand | CBE Competency | Activity evidence |
|------------|--------------|-------------------|
| Design | Creativity | Learners design their version of the deliverable. |
| Code | Digital Literacy + Critical Thinking | Writing and debugging code in {tool}. |
| Create | Self-efficacy | Producing a working artifact by the end of the lesson. |
| Connect | Citizenship | Conservation message tied to the {species}. |
| Evaluate | Learning to Learn | Glow/grow peer feedback and reflection checklist. |
"""
    path = LESSONS_DIR / f"lesson-{number:02d}-{slug}.md"
    path.write_text(content, encoding='utf-8')
    print(f"Wrote {path}")

print(f"Done: generated {len(MODULES)-1} lesson plan files.")
