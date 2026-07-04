"""
Mako Coders Quiz Dashboard

A lightweight Flask app that:
- Parses weekly quizzes from ../quizzes/
- Lets students take quizzes and auto-scores answers
- Tracks completion, scores, and achievements in SQLite
- Renders a printable, professional-yet-fun dashboard

Run:
    cd dashboard
    pip install -r requirements.txt
    python3 app.py

Open http://127.0.0.1:5000
"""
from __future__ import annotations

import json
import os
import re
import sqlite3
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

# --- Paths ---------------------------------------------------------------
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
QUIZZES_DIR = ROOT / "quizzes"
DATA_DIR = HERE / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "dashboard.db"

# --- Flask app -----------------------------------------------------------
app = Flask(__name__)
app.secret_key = os.environ.get("MAKOCODERS_SECRET", "mako-shark-2026-dev-key")


# --- Data models ---------------------------------------------------------
@dataclass
class Question:
    number: int
    text: str
    answer: str


@dataclass
class Quiz:
    week: int
    slug: str
    title: str
    age_band: str  # "10-13" or "14-17"
    questions: list[Question] = field(default_factory=list)


# --- Quiz parsing --------------------------------------------------------
def parse_quiz(path: Path) -> Quiz | None:
    """Parse a quiz markdown file into a Quiz object."""
    text = path.read_text(encoding="utf-8")
    # Header: "# Week NN Quiz — Title — Ages X–Y"
    header_match = re.match(
        r"^#\s+Week\s+(\d+)\s+Quiz\s+—\s+(.+?)\s+—\s+Ages\s+(.+?)\n",
        text,
        re.IGNORECASE,
    )
    if not header_match:
        return None
    week = int(header_match.group(1))
    title = header_match.group(2).strip()
    age_label = header_match.group(3).strip()
    age_band = "10-13" if "10" in age_label else "14-17"

    # Slug from filename: quiz-NN-slug-age.md
    slug = path.stem.split("-", 3)[2]

    # Split questions and answer key sections
    q_section_match = re.search(r"##\s*Questions\n(.*?)(?=##\s*Answer\s*Key|$)", text, re.S | re.I)
    a_section_match = re.search(r"##\s*Answer\s*Key\n(.*)$", text, re.S | re.I)
    if not q_section_match or not a_section_match:
        return None

    q_lines = [ln.strip() for ln in q_section_match.group(1).strip().splitlines() if ln.strip()]
    a_lines = [ln.strip() for ln in a_section_match.group(1).strip().splitlines() if ln.strip()]

    questions: list[Question] = []
    q_pattern = re.compile(r"^(\d+)\.\s*(.*)$")
    answers = {}
    for ln in a_lines:
        m = q_pattern.match(ln)
        if m:
            answers[int(m.group(1))] = m.group(2).strip()

    for ln in q_lines:
        m = q_pattern.match(ln)
        if m:
            num = int(m.group(1))
            questions.append(
                Question(number=num, text=m.group(2).strip(), answer=answers.get(num, ""))
            )

    return Quiz(week=week, slug=slug, title=title, age_band=age_band, questions=questions)


def load_all_quizzes() -> list[Quiz]:
    """Load every quiz file from ../quizzes/."""
    quizzes: list[Quiz] = []
    if QUIZZES_DIR.exists():
        for path in sorted(QUIZZES_DIR.glob("*.md")):
            quiz = parse_quiz(path)
            if quiz and quiz.questions:
                quizzes.append(quiz)
    return quizzes


def quizzes_by_week(quizzes: list[Quiz]) -> dict[int, dict[str, Quiz]]:
    """Group quizzes by week and age band."""
    out: dict[int, dict[str, Quiz]] = {}
    for q in quizzes:
        out.setdefault(q.week, {})[q.age_band] = q
    return out


# --- Database ------------------------------------------------------------
def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age_band TEXT NOT NULL CHECK(age_band IN ('10-13', '14-17')),
            grade TEXT,
            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            week INTEGER NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            percent INTEGER NOT NULL,
            answers TEXT NOT NULL,
            taken_at TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id)
        );

        CREATE TABLE IF NOT EXISTS achievements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            badge TEXT NOT NULL,
            awarded_at TEXT NOT NULL,
            UNIQUE(student_id, badge)
        );
        """
    )
    conn.commit()
    conn.close()


# --- Achievement logic ---------------------------------------------------
BADGES = {
    "first_splash": {"name": "First Splash", "icon": "🌊", "desc": "Completed your first quiz."},
    "tide_pool": {"name": "Tide Pool Scout", "icon": "🦀", "desc": "Completed 5 quizzes."},
    "coral_reef": {"name": "Coral Reef Builder", "icon": "🪸", "desc": "Completed 12 quizzes."},
    "open_ocean": {"name": "Open Ocean Diver", "icon": "🐬", "desc": "Completed 26 quizzes."},
    "mako_hunter": {"name": "Mako Hunter", "icon": "🦈", "desc": "Completed 40 quizzes."},
    "perfect_week": {"name": "Perfect Week", "icon": "⭐", "desc": "Scored 100% on any quiz."},
    "steady_current": {"name": "Steady Current", "icon": "🌊", "desc": "Completed quizzes 4 weeks in a row."},
    "conservation_champion": {"name": "Conservation Champion", "icon": "🌍", "desc": "Completed the Week 52 Mako quiz."},
}


def check_and_award_badges(student_id: int):
    """Evaluate and record new badges for a student."""
    conn = get_db()
    cursor = conn.cursor()

    # Total completed quizzes (distinct weeks)
    cursor.execute(
        "SELECT COUNT(DISTINCT week) FROM attempts WHERE student_id = ?", (student_id,)
    )
    completed = cursor.fetchone()[0]

    # Any perfect score?
    cursor.execute(
        "SELECT EXISTS(SELECT 1 FROM attempts WHERE student_id = ? AND percent = 100)",
        (student_id,),
    )
    has_perfect = cursor.fetchone()[0]

    # Completed week 52?
    cursor.execute(
        "SELECT EXISTS(SELECT 1 FROM attempts WHERE student_id = ? AND week = 52)",
        (student_id,),
    )
    completed_52 = cursor.fetchone()[0]

    # Current badges
    cursor.execute("SELECT badge FROM achievements WHERE student_id = ?", (student_id,))
    existing = {row["badge"] for row in cursor.fetchall()}

    new_badges: list[tuple[int, str, str]] = []
    now = datetime.now().isoformat(timespec="seconds")

    thresholds = [
        ("first_splash", completed >= 1),
        ("tide_pool", completed >= 5),
        ("coral_reef", completed >= 12),
        ("open_ocean", completed >= 26),
        ("mako_hunter", completed >= 40),
        ("perfect_week", has_perfect),
        ("conservation_champion", completed_52),
    ]

    for badge, condition in thresholds:
        if condition and badge not in existing:
            new_badges.append((student_id, badge, now))
            cursor.execute(
                "INSERT INTO achievements (student_id, badge, awarded_at) VALUES (?, ?, ?)",
                (student_id, badge, now),
            )

    # Steady current: at least 4 distinct weeks with no gap > 7 days
    cursor.execute(
        "SELECT DISTINCT taken_at FROM attempts WHERE student_id = ? ORDER BY taken_at",
        (student_id,),
    )
    dates = [datetime.fromisoformat(row["taken_at"]) for row in cursor.fetchall()]
    if len(dates) >= 4:
        max_gap = max(
            (dates[i] - dates[i - 1]).days for i in range(1, len(dates))
        )
        if max_gap <= 7 and "steady_current" not in existing:
            cursor.execute(
                "INSERT INTO achievements (student_id, badge, awarded_at) VALUES (?, ?, ?)",
                (student_id, "steady_current", now),
            )

    conn.commit()
    conn.close()


def get_achievements(student_id: int) -> list[dict]:
    """Return awarded badge details for a student."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT badge, awarded_at FROM achievements WHERE student_id = ? ORDER BY awarded_at",
        (student_id,),
    )
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "badge": row["badge"],
            "awarded_at": row["awarded_at"],
            **BADGES.get(row["badge"], {}),
        }
        for row in rows
    ]


# --- Helpers -------------------------------------------------------------
def get_student_stats(student_id: int) -> dict:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT week, MAX(percent) as best_percent, COUNT(*) as attempts
        FROM attempts
        WHERE student_id = ?
        GROUP BY week
        ORDER BY week
        """,
        (student_id,),
    )
    rows = cursor.fetchall()
    conn.close()
    total_attempts = sum(r["attempts"] for r in rows)
    completed_weeks = len(rows)
    avg_best = round(sum(r["best_percent"] for r in rows) / completed_weeks) if completed_weeks else 0
    return {
        "completed_weeks": completed_weeks,
        "total_attempts": total_attempts,
        "average_best": avg_best,
        "week_details": [dict(r) for r in rows],
    }


# --- Routes --------------------------------------------------------------
@app.route("/")
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, age_band, grade, created_at FROM students ORDER BY created_at DESC"
    )
    students = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return render_template("index.html", students=students)


@app.route("/student/add", methods=["POST"])
def add_student():
    name = request.form.get("name", "").strip()
    age_band = request.form.get("age_band", "10-13").strip()
    grade = request.form.get("grade", "").strip()
    if name and age_band in ("10-13", "14-17"):
        conn = get_db()
        conn.execute(
            "INSERT INTO students (name, age_band, grade, created_at) VALUES (?, ?, ?, ?)",
            (name, age_band, grade, datetime.now().isoformat(timespec="seconds")),
        )
        conn.commit()
        conn.close()
    return redirect(url_for("index"))


@app.route("/student/<int:student_id>")
def student_dashboard(student_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()
    conn.close()
    if not student:
        return "Student not found", 404

    quizzes = load_all_quizzes()
    grouped = quizzes_by_week(quizzes)
    stats = get_student_stats(student_id)
    achievements = get_achievements(student_id)

    return render_template(
        "dashboard.html",
        student=dict(student),
        grouped=grouped,
        stats=stats,
        achievements=achievements,
    )


@app.route("/quiz/<int:student_id>/<int:week>", methods=["GET", "POST"])
def take_quiz(student_id: int, week: int):
    quizzes = load_all_quizzes()
    grouped = quizzes_by_week(quizzes)
    week_quizzes = grouped.get(week, {})
    if not week_quizzes:
        return "Quiz not found", 404

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()
    conn.close()
    if not student:
        return "Student not found", 404

    # Pick the age-appropriate quiz, falling back to 10-13 if missing
    quiz = week_quizzes.get(student["age_band"]) or week_quizzes.get("10-13")

    if not quiz:
        return redirect(url_for("index"))
    if request.method == "POST":
        answers = {}
        score = 0
        for q in quiz.questions:
            submitted = request.form.get(f"q{q.number}", "").strip()
            answers[q.number] = submitted
            # Simple scoring: case-insensitive substring match on key terms
            if score_answer(submitted, q.answer):
                score += 1
        total = len(quiz.questions)
        percent = round((score / total) * 100) if total else 0
        now = datetime.now().isoformat(timespec="seconds")

        conn = get_db()
        conn.execute(
            "INSERT INTO attempts (student_id, week, score, total, percent, answers, taken_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (student_id, week, score, total, percent, json.dumps(answers), now),
        )
        conn.commit()
        conn.close()
        check_and_award_badges(student_id)
        return redirect(url_for("quiz_result", student_id=student_id, week=week))

    return render_template("quiz.html", student=dict(student), quiz=quiz)


def score_answer(submitted: str, expected: str) -> bool:
    """
    Score a submitted answer against the answer key.
    - Exact match after normalisation, or
    - Submitted contains enough key words from the expected answer.
    """
    submitted = submitted.lower().strip(".,!?")
    expected = expected.lower().strip(".,!?")
    if submitted == expected:
        return True
    # For numeric or very short answers, require exact match.
    if len(expected) <= 3 and expected.replace(" ", "").isdigit():
        return submitted == expected

    # Split expected into content words and check majority presence.
    stop = {"the", "a", "an", "is", "are", "to", "of", "and", "or", "it", "that", "for"}
    words = [w for w in re.findall(r"[a-z0-9]+", expected) if w not in stop and len(w) > 2]
    if not words:
        return submitted == expected
    hits = sum(1 for w in words if w in submitted)
    return hits >= max(1, round(len(words) * 0.6))


@app.route("/result/<int:student_id>/<int:week>")
def quiz_result(student_id: int, week: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM attempts WHERE student_id = ? AND week = ? ORDER BY taken_at DESC LIMIT 1",
        (student_id, week),
    )
    attempt = cursor.fetchone()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()
    conn.close()
    if not attempt or not student:
        return "Result not found", 404

    quizzes = load_all_quizzes()
    grouped = quizzes_by_week(quizzes)
    quiz = grouped.get(week, {}).get(student["age_band"]) or grouped.get(week, {}).get("10-13")
    if not quiz:
        return "Quiz not found", 404

    answers = json.loads(attempt["answers"])
    return render_template(
        "result.html",
        student=dict(student),
        attempt=dict(attempt),
        quiz=quiz,
        answers=answers,
        score_answer=score_answer,
    )


@app.route("/print/<int:student_id>")
def print_report(student_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()
    conn.close()
    if not student:
        return "Student not found", 404
    stats = get_student_stats(student_id)
    achievements = get_achievements(student_id)
    return render_template(
        "print_report.html",
        student=dict(student),
        stats=stats,
        achievements=achievements,
        generated_at=datetime.now().strftime("%d %B %Y"),
    )


# --- Init ----------------------------------------------------------------
@app.cli.command("init")
def init_command():
    init_db()
    print("Database initialised at", DB_PATH)


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=True)
