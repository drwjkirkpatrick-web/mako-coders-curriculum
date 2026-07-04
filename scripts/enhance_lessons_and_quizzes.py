"""
Generate quiz files and enhance lesson plans for Mako Coders.

This script:
1. Creates two quiz files per week (ages 10-13 and 14-17) in quizzes/.
2. Inserts Extra Credit, Homework, and Weekly Quiz sections into each lesson plan.

Run: python3 scripts/enhance_lessons_and_quizzes.py
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / 'tests'))
from modules import MODULES

QUIZZES_DIR = ROOT / 'quizzes'
LESSONS_DIR = ROOT / 'lessons'

QUIZZES_DIR.mkdir(exist_ok=True)


def quiz_for(week: int, title: str, species: str, strand: str, tool: str):
    """Return a list of 10 (question, answer) items for the given week and age band."""

    # Base facts derived from module metadata
    swahili = {
        'Shortfin mako shark': 'papa mako',
        'Green sea turtle': 'kobe ya kijani',
        'Hawksbill sea turtle': 'kobe ya pwani',
        'Spinner dolphin': 'pomboo',
        'Indian Ocean humpback dolphin': 'pomboo ya Bahari Hindi',
        'Coral reefs': 'miamba',
        'Whale shark': 'papa mafia',
        'Dugong': 'dugong',
        'Humpback whale': 'nyangumi',
        'Seagrass beds': 'mwani wa baharini',
        'Mangroves': 'mikoko',
    }.get(species, 'viumbe vya baharini')

    # Concept keywords by week group
    if week <= 13:
        concept = 'block-based coding in Scratch'
        key_idea = 'sequencing, loops, events, and debugging'
    elif week <= 26:
        concept = 'text-based Python and data structures'
        key_idea = 'variables, lists, dictionaries, and visualisation'
    elif week <= 39:
        concept = 'physical computing and networking'
        key_idea = 'sensors, outputs, radio, and internet basics'
    else:
        concept = 'capstone project development'
        key_idea = 'functions, classes, game loops, and conservation messaging'

    # Age 10-13 quiz: concrete, recall + simple application
    young = [
        (f"What is the Swahili name for the {species}?", swahili),
        (f"Which country does the {species} live near in our lessons?", "Kenya, along the Indian Ocean coast."),
        ("What does 'conservation' mean?", "Protecting animals and their habitats so they do not disappear."),
        (f"What coding tool do we mainly use in Week {week:02d}?", tool),
        (f"What is one new word or idea we learned this week about {key_idea}?", f"[Teacher checks: concept from {title}]"),
        ("Why is it important to test your code often?", "So you can find mistakes early and fix them."),
        ("Name one thing humans do that can harm the ocean.", "Plastic pollution, overfishing, or destroying mangroves and coral reefs."),
        ("What is a 'habitat'?", "The place where an animal lives and finds food and shelter."),
        (f"How does the {species} help us understand coding?", f"It gives us a real example for {concept}."),
        ("What is one way you can share your project to help others?", "Show it to classmates, family, or post a picture with a conservation message."),
    ]

    # Age 14-17 quiz: more abstract, analysis, design
    teen = [
        (f"Describe the real-world significance of the {species} for Kenyan marine ecosystems.", "[Teacher checks: habitat/role/conservation note from the lesson]"),
        (f"How does learning about the {species} connect to the CBE strand '{strand}'?", f"[Teacher checks: link to {concept}]"),
        ("Explain the difference between a syntax error and a logic error.", "A syntax error breaks the rules of the language; a logic error runs but gives the wrong result."),
        (f"Give one example of how you used {key_idea} in this week's project.", "[Teacher checks: project-specific response]"),
        ("Why is data privacy important when sharing wildlife locations?", "Exact locations can help poachers or disturb sensitive habitats."),
        (f"Compare block-based Scratch with text-based Python for teaching {concept}.", "Blocks are visual and beginner-friendly; text is precise, portable, and closer to professional coding."),
        ("Describe one ethical consideration when using technology for conservation.", "Avoid sharing sensitive locations, give credit for data, and respect community knowledge."),
        ("How would you test whether a loop is working correctly?", "Check the start value, the stop condition, and the change made each repetition."),
        ("What is one benefit of writing reusable functions or blocks?", "You write less code, reduce mistakes, and can reuse the logic in other projects."),
        (f"Design a one-sentence conservation message for a project about the {species}.", "[Teacher checks: original, fact-based conservation message]"),
    ]

    return {"10-13": young, "14-17": teen}


def write_quiz(week: int, slug: str, title: str, species: str, strand: str, tool: str, age_band: str):
    """Write a single quiz markdown file with real questions."""
    items = quiz_for(week, title, species, strand, tool)[age_band]
    age_label = "Ages 10–13" if age_band == "10-13" else "Ages 14–17"
    lines = [
        f"# Week {week:02d} Quiz — {title} — {age_label}",
        "",
        f"> *10 questions to check understanding of Week {week:02d}: {title}.*",
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
    return path


def tool_for_week(week: int):
    """Return the primary tool for a given week."""
    if week <= 13:
        return "Scratch 3"
    elif week <= 26:
        return "Python + Turtle"
    elif week <= 39:
        return "micro:bit / MakeCode"
    else:
        return "Python + Pygame Zero"


def extra_credit_and_homework(week: int, title: str, species: str, tier: str):
    """Return (extra_credit_md, homework_md) for the week."""
    extra = f"""**Design a second scene.** Create a short Scratch animation or Python sketch that shows the {species} at a different time of day (dawn, noon, or night). Add at least one new sprite or shape and explain in one sentence why you chose that time."""
    homework = f"""Spend 15–20 minutes at home exploring the {species} online or in a book. Write down one new fact and one question you would like to ask Mako next week. Bring your fact and question to class."""

    lower = title.lower()
    if "showcase" in lower or "reflection" in lower:
        extra = f"""**Peer mentor.** Help a classmate finish or improve their project. Write two sentences describing what you taught and what you learned by teaching."""
        homework = f"""Prepare a 60-second speech about your favourite project from this term. Practice in front of a mirror or with a family member."""
    elif "capstone" in lower or "mako shark expedition" in lower or "planning" in lower:
        extra = f"""**Add a level or mode.** Introduce a second difficulty level, a new Kenyan species, or a data-export feature to your Mako Shark Expedition. Document the change in your project README."""
        homework = f"""Work on your capstone for 20–30 minutes at home. Fix one bug or add one small feature. Be ready to share what changed."""
    elif any(k in lower for k in ["data", "survey", "plot", "filter", "list", "dictionary"]):
        extra = f"""**Collect your own data.** Record three real or realistic observations about marine life near your community (or from a video). Add them to your project data file and explain any trends you notice."""
        homework = f"""Find one real news article or report about Kenyan marine conservation. Summarise it in 3–5 sentences and note any numbers or data mentioned."""
    elif any(k in lower for k in ["micro:bit", "sensor", "radio", "input", "output", "temperature", "compass", "tide-guard"]):
        extra = f"""**Build a sensor alarm.** Extend your micro:bit project so it reacts to two different inputs (for example, temperature + button press) and shows different LED patterns for each."""
        homework = f"""Draw a labelled diagram of your micro:bit circuit or project idea. Label the input, the processing, and the output."""
    elif "function" in lower:
        extra = f"""**Write a helper function.** Create a reusable function that draws or describes a different marine species. Call it at least three times with different inputs."""
        homework = f"""Write down one everyday task that repeats (e.g., making tea). Break it into a function with 3–4 steps. Bring the steps to class."""
    elif "loop" in lower or "pattern" in lower:
        extra = f"""**Nested pattern challenge.** Use one loop inside another to draw a coral reef tile or turtle-shell pattern with at least 6 shapes."""
        homework = f"""Count how many times you repeat an action at home today (brushing teeth, climbing stairs). Write the number and one way a loop could model it."""
    elif any(k in lower for k in ["conditional", "branching", "humpback", "dolphin"]):
        extra = f"""**Multi-species identifier.** Add one more species to your conditional decision tree and test it with three different inputs."""
        homework = f"""List three if/then rules you follow at home or school. Convert one of them into pseudocode or Scratch blocks."""
    elif "variable" in lower:
        extra = f"""**Tracker with history.** Store three measurements in separate variables and display the average. Explain why using a variable is better than hard-coding the numbers."""
        homework = f"""Find two numbers you track in daily life (time, score, temperature). Write them as variables and show how they could change."""
    elif "event" in lower:
        extra = f"""**Two-player event.** Add a second keyboard-controlled sprite and make the two sprites react differently to the same event."""
        homework = f"""Observe one event in nature or your home (a door opening, rain starting). Write what caused it and what happened as a result."""
    elif "debug" in lower:
        extra = f"""**Bug bounty.** Create a short program with one deliberate bug, swap with a partner, and see who can find and fix it fastest."""
        homework = f"""Write down one mistake you made while coding today and how you fixed it. Bring it to share."""
    elif "decompose" in lower:
        extra = f"""**Sub-task map.** Draw a flowchart with at least four sub-tasks for a real conservation action such as a beach cleanup."""
        homework = f"""Choose a chore at home. List the steps in order and circle any step that could be shared with someone else."""
    elif any(k in lower for k in ["class", "object", "coral reef"]):
        extra = f"""**New species class.** Add a second class (e.g., Fish or SeagrassPatch) with at least two attributes and one method. Make it interact with the Coral class."""
        homework = f"""Pick three real objects in your room. For each one, list two properties and one action it can do."""
    elif any(k in lower for k in ["api", "internet", "network"]):
        extra = f"""**Offline fact cache.** Build a small dictionary of five Kenyan ocean facts that your program can use even without internet."""
        homework = f"""Ask a family member how they use the internet safely. Write down one tip they shared."""
    elif any(k in lower for k in ["security", "cyber", "password"]):
        extra = f"""**Password strength checker.** Write a simple program that tells the user if a password is weak, medium, or strong based on length and character types."""
        homework = f"""Review your own passwords or passphrases at home. Make sure none are shared across important accounts."""
    elif any(k in lower for k in ["citizenship", "ethics", "clean coast"]):
        extra = f"""**Campaign slide.** Design one poster or slide that teaches others how to protect marine species using technology responsibly."""
        homework = f"""Think of one way technology can harm nature if used badly. Write two sentences about how to avoid that harm."""
    elif "game loop" in lower:
        extra = f"""**Smooth movement.** Make the mako shark accelerate smoothly instead of jumping, and add a boundary so it cannot leave the screen."""
        homework = f"""Play any simple game for 10 minutes. List three events (key press, collision, score) that the game must handle."""
    elif any(k in lower for k in ["ui", "accessibility", "interface"]):
        extra = f"""**Screen-reader friendly.** Add text labels to all visual elements and test whether a friend can understand the project without seeing the images."""
        homework = f"""Look at one app or website you use. Find one feature that helps people with different abilities."""
    elif any(k in lower for k in ["presentation", "rehearsal"]):
        extra = f"""**Demo video.** Record a 60-second screen-capture or phone video of your project working and narrate what it does."""
        homework = f"""Practice your presentation three times. Time yourself and ask someone for one piece of feedback."""
    elif "blocks to text" in lower:
        extra = f"""**Translate a Scratch block.** Pick any three Scratch blocks you used in Term 1 and write the equivalent Python code."""
        homework = f"""Install Python on a home computer or use an online Python editor. Run one print() statement and show the output."""
    elif "whale song" in lower:
        extra = f"""**Compose a short song.** Create a list of 8–10 notes or frequencies and make your program play or visualise them."""
        homework = f"""Listen to a recording of a humpback whale song. Write three words that describe how it sounds."""
    elif "automate" in lower:
        extra = f"""**Schedule a log.** Make your program append a new line to a file every time it runs, with a timestamp."""
        homework = f"""Write down one chore you do daily. List the steps and identify one that a computer could remind you about."""

    return extra.strip(), homework.strip()


def insert_sections(lesson_path: Path, week: int, slug: str, title: str, species: str, tier: str):
    """Insert Extra Credit, Homework, and Weekly Quiz sections into a lesson plan."""
    text = lesson_path.read_text(encoding='utf-8')

    # Skip if already updated
    if "## Extra Credit Challenge" in text:
        return False

    extra, homework = extra_credit_and_homework(week, title, species, tier)

    new_section = f"""
## Extra Credit Challenge

{extra}

## Homework Assignment

{homework}

## Weekly Quiz

- Ages 10–13: [`quizzes/quiz-{week:02d}-{slug}-10-13.md`](../../quizzes/quiz-{week:02d}-{slug}-10-13.md)
- Ages 14–17: [`quizzes/quiz-{week:02d}-{slug}-14-17.md`](../../quizzes/quiz-{week:02d}-{slug}-14-17.md)

*The quiz includes 10 questions and an answer key to check understanding before the next lesson.*
"""

    # Insert just before "## Differentiation"
    text = re.sub(
        r"(\n## Differentiation\n)",
        new_section + r"\1",
        text,
        count=1,
    )
    lesson_path.write_text(text, encoding='utf-8')
    return True


# Main execution
updated = 0
for number, slug, title, species, tier, age, strand in MODULES:
    tool = tool_for_week(number)
    write_quiz(number, slug, title, species, strand, tool, "10-13")
    write_quiz(number, slug, title, species, strand, tool, "14-17")
    lesson_path = LESSONS_DIR / f"lesson-{number:02d}-{slug}.md"
    if insert_sections(lesson_path, number, slug, title, species, tier):
        updated += 1
        print(f"Updated lesson {number:02d}")

print(f"\nDone: wrote {len(MODULES) * 2} quiz files and updated {updated} lesson plans.")
