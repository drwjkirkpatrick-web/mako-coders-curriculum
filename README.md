# Mako Coders Curriculum

> *A 52-week, once-per-week coding curriculum for Kenyan learners, aligned to Kenya’s Competency-Based Education (CBE) framework and inspired by the real marine life of the Kenyan coast. Final project: the Mako Shark Expedition.*

---

## Quick facts

| Item | Detail |
|------|--------|
| **Target learners** | CBE Junior School (Grade 7–9) and Senior School STEM beginners |
| **Session length** | 2 hours, once per week, with one 10-minute break |
| **Total weeks** | 52 |
| **Final project** | Mako Shark Expedition — a conservation-themed game/dashboard |
| **Themes** | Kenyan ocean wildlife: spinner dolphins, sea turtles, whale sharks, dugongs, coral reefs, mangroves, and the shortfin mako shark |
| **Tool progression** | Scratch 3 → Python + Turtle → micro:bit → Python + Pygame Zero |
| **Pedagogy** | CBE strands + RPF Digital Making (Design, Code, Create, Connect, Evaluate) |

---

## What makes this curriculum different

1. **Kenyan context first.** Every module uses a real species documented off the Kenyan coast, with local (Swahili) names and conservation notes from sources such as IFAW, Kenya Wildlife Service, and WCS.
2. **CBE-aligned from day one.** Each lesson maps to a CBE strand, develops the 7 core competencies, and uses the BE/AE/ME/EE rubric.
3. **Offline-ready.** The curriculum assumes intermittent connectivity. Scratch offline editor, Python on Raspberry Pi / old laptops, and micro:bit simulators are all valid pathways.
4. **Final project with purpose.** The Mako Shark Expedition teaches learners to combine loops, conditionals, functions, data, and conservation messaging into a playable or explorable artifact.
5. **Built-in assessment for two age bands.** Every lesson includes an Extra Credit Challenge, a Homework Assignment, and two 10-question quizzes — one for ages 10–13 and one for ages 14–17. The quizzes are code-focused and mapped to CBE strands, with answer keys and auto-scoring through the local dashboard.

---

## Repository layout

```
mako-coders-curriculum/
├── prompts/                # 52 testable AI-tutor system prompts
│   ├── PROMPT-TEMPLATE.md
│   ├── 04-dolphin-loops.md
│   └── ...
├── lessons/                # 52 CBE-aligned lesson plans
│   ├── LESSON-TEMPLATE.md
│   ├── lesson-04-dolphin-loops.md
│   └── ...
├── quizzes/                # 104 weekly quizzes (10 questions × 2 age bands)
│   ├── quiz-04-dolphin-loops-10-13.md
│   └── quiz-04-dolphin-loops-14-17.md
├── dashboard/              # Local Flask dashboard: auto-score quizzes + achievements + printable reports
│   ├── app.py
│   ├── smoke_test.py
│   ├── requirements.txt
│   ├── templates/
│   ├── static/css/
│   └── data/
├── research/               # Domain research + standards mapping
│   ├── standards-mapping.md
│   ├── domain-reference.md
│   └── module-plan.md
├── scripts/                # Generator scripts
│   ├── generate_prompts.py
│   ├── generate_lessons.py
│   └── enhance_lessons_and_quizzes.py
├── tests/                  # Validation harness
│   ├── modules.py          # Master module metadata
│   └── test_prompts.py     # CLI validator
├── tracker/                # SQLite progress tracker + HTML reports
│   └── progress_tracker.py
├── README.md
├── LICENSE
└── .gitignore
```

---

## Getting started

### 1. Validate curriculum files

```bash
cd ~/projects/mako-coders-curriculum
python3 tests/test_prompts.py --summary
python3 tests/test_prompts.py --validate --non-interactive
```

### 2. Try a single prompt

```bash
python3 tests/test_prompts.py --prompt 4
```

### 3. Run the local quiz dashboard

```bash
cd dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Open http://127.0.0.1:5000
- Add students by age band (10–13 or 14–17).
- Take weekly quizzes; answers are auto-scored against the answer key.
- View badges, completion records, and a printable student report.
- Run `python3 smoke_test.py` to verify the dashboard without a browser.

### 4. Initialise the progress tracker

```bash
python3 tracker/progress_tracker.py init
python3 tracker/progress_tracker.py add-student "Amina Juma" Grade8
python3 tracker/progress_tracker.py record 1 4 ME
python3 tracker/progress_tracker.py badges 1
python3 tracker/progress_tracker.py report --student 1
```

---

## The 52-week arc

| Term | Weeks | Focus | Capstone milestone |
|------|-------|-------|-------------------|
| **Ocean Foundations** | 1–13 | Sequencing, variables, loops, conditionals, events, debugging | Animated ocean scene |
| **Data & Coastal Systems** | 14–26 | Lists, dictionaries, data visualisation, file I/O | Marine data explorer |
| **Hardware & Networks** | 27–39 | micro:bit sensors, radio networks, APIs, cybersecurity | Tide-guard sensor station |
| **Conservation & Capstone** | 40–52 | Functions, classes, project cycle, peer review | **Mako Shark Expedition** |

See `research/module-plan.md` for the full week-by-week breakdown.

---

## Assessment

CBE uses a four-level rubric:

| Band | Label | Range |
|------|-------|-------|
| BE | Below Expectations | 0–39% |
| AE | Approaching Expectations | 40–59% |
| ME | Meeting Expectations | 60–79% |
| EE | Exceeding Expectations | 80–100% |

Every lesson plan contains:
- a criterion-based assessment table
- an **Extra Credit Challenge** for early finishers
- a **Homework Assignment** to reinforce the week's concept
- two **Weekly Quizzes** (ages 10–13 and 14–17) with code-focused questions, answer keys, and CBE strand mapping

The progress tracker auto-awards badges when learners reach ME or EE. The dashboard auto-scores quiz answers against each answer key.

---

## Badge tiers

| Tier | Theme | Example badges |
|------|-------|----------------|
| Tide Pool | Beginner | Ocean Setup, Looper, Decision Maker, Debugger |
| Coral Reef | Builder | Data Diver, List Master, Mapper, Visualiser |
| Open Ocean | Developer | Sensor Scout, Radio Ranger, Network Navigator |
| Mako Hunter | Advanced | Expedition Leader, Game Loop Guru, Conservation Champion |
| Core Competency | Transversal | Communicator, Problem Solver, Digital Citizen |

---

## Standards alignment

- Kenya CBE 2-6-3-3 structure
- CBE 7 core competencies
- CBE assessment rubric (BE/AE/ME/EE)
- Computer Studies / ICT strands: Algorithms, Data, Computers, Networks, Security
- Raspberry Pi Foundation Digital Making strands

Full mapping: `research/standards-mapping.md`

---

## Marine life sources

- IFAW — *Safeguarding coastal ecosystems in Kenya* and 2023 aerial megafauna survey
- WCS — *Rare climate refuge for coral reefs discovered off Kenya and Tanzania*
- WWF — Southwest Indian Ocean seascape
- NOAA Fisheries — Shortfin mako shark biology
- IUCN / IOTC — Indian Ocean shortfin mako assessment

Full species reference: `research/domain-reference.md`

---

## Contributing

1. Add or improve a prompt in `prompts/`.
2. Add or improve a lesson in `lessons/`.
3. Update `tests/modules.py` if module numbers or slugs change.
4. Run `python3 tests/test_prompts.py --validate --non-interactive` before committing.

---

## License

MIT — see `LICENSE`.

---

*Version 1.0.0 — July 2026. Created for Kenyan learners who love the ocean and want to code it to life.*
