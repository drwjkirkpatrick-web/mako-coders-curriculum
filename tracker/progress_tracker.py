#!/usr/bin/env python3
"""
Progress tracker for Mako Coders.

Features:
- SQLite database for students, modules, and badges.
- Register students and record progress per week.
- Auto-award badges when learners reach ME or EE on relevant modules.
- Printable HTML reports for a student or the whole class.

Usage:
    python3 tracker/progress_tracker.py init
    python3 tracker/progress_tracker.py add-student "Amina Juma" Grade8
    python3 tracker/progress_tracker.py record 1 4 ME
    python3 tracker/progress_tracker.py badges 1
    python3 tracker/progress_tracker.py report --student 1
    python3 tracker/progress_tracker.py report --class

Heavily commented for teachers and maintainers.
"""

import argparse
import os
import sqlite3
import sys
from pathlib import Path

# Add project root so we can import module metadata
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tests"))

from modules import MODULES  # noqa: E402

DB_PATH = ROOT / "tracker" / "mako_coders.db"

# Badges are grouped by tier and map to the week numbers required.
BADGES = [
    # Tide Pool tier
    ("Ocean Setup", "Tide Pool", [1]),
    ("Sequencer", "Tide Pool", [2]),
    ("Looper", "Tide Pool", [4]),
    ("Decision Maker", "Tide Pool", [6]),
    ("Debugger", "Tide Pool", [10]),
    # Coral Reef tier
    ("Data Diver", "Coral Reef", [15]),
    ("List Master", "Coral Reef", [16]),
    ("Mapper", "Coral Reef", [18]),
    ("Function Fan", "Coral Reef", [20]),
    ("Visualiser", "Coral Reef", [23]),
    # Open Ocean tier
    ("Sensor Scout", "Open Ocean", [28]),
    ("Radio Ranger", "Open Ocean", [31]),
    ("Network Navigator", "Open Ocean", [33]),
    ("Security Guard", "Open Ocean", [37]),
    ("Citizen Coder", "Open Ocean", [38]),
    # Mako Hunter tier
    ("Expedition Leader", "Mako Hunter", [40]),
    ("Function Pro", "Mako Hunter", [41]),
    ("Class Captain", "Mako Hunter", [42]),
    ("Game Loop Guru", "Mako Hunter", [44]),
    ("Conservation Champion", "Mako Hunter", [52]),
    # Core competency badges (transversal)
    ("Communicator", "Core Competency", [13, 39, 50, 51]),
    ("Problem Solver", "Core Competency", [10, 11, 43]),
    ("Creative Coder", "Core Competency", [12, 36, 45]),
    ("Digital Citizen", "Core Competency", [25, 37, 38]),
    ("Lifelong Learner", "Core Competency", [13, 39]),
    ("Self-starter", "Core Competency", [1, 40]),
]


def get_db():
    """Open the SQLite database, creating it if necessary."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create the tables required for the tracker."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            grade TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            week_number INTEGER NOT NULL,
            band TEXT NOT NULL CHECK(band IN ('BE','AE','ME','EE')),
            notes TEXT,
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students(id),
            UNIQUE(student_id, week_number)
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS badges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            badge_name TEXT NOT NULL,
            tier TEXT NOT NULL,
            awarded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students(id),
            UNIQUE(student_id, badge_name)
        )
        """
    )
    conn.commit()
    conn.close()
    print(f"Database initialised at {DB_PATH}")


def add_student(name: str, grade: str):
    """Register a new student."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (full_name, grade) VALUES (?, ?)",
        (name, grade),
    )
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    print(f"Added student '{name}' (ID {student_id}, Grade {grade})")


def record_progress(student_id: int, week: int, band: str, notes: str = ""):
    """Record a CBE band for a student on a given week."""
    band = band.upper()
    if band not in ("BE", "AE", "ME", "EE"):
        print("Band must be one of BE, AE, ME, EE.")
        return 1
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO progress (student_id, week_number, band, notes)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(student_id, week_number)
        DO UPDATE SET band=excluded.band, notes=excluded.notes, recorded_at=CURRENT_TIMESTAMP
        """,
        (student_id, week, band, notes),
    )
    conn.commit()
    conn.close()
    print(f"Recorded Week {week} = {band} for student {student_id}")
    # Re-check badges after any progress update
    award_badges(student_id)
    return 0


def award_badges(student_id: int):
    """Award any badges the student has earned."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT week_number, band FROM progress WHERE student_id = ?",
        (student_id,),
    )
    progress = {row["week_number"]: row["band"] for row in cursor.fetchall()}

    new_badges = []
    for badge_name, tier, required_weeks in BADGES:
        # Badge requires ME or EE on at least one required week
        earned = any(
            progress.get(w) in ("ME", "EE") for w in required_weeks
        )
        if earned:
            try:
                cursor.execute(
                    """
                    INSERT INTO badges (student_id, badge_name, tier)
                    VALUES (?, ?, ?)
                    """,
                    (student_id, badge_name, tier),
                )
                new_badges.append((badge_name, tier))
            except sqlite3.IntegrityError:
                pass  # already awarded
    conn.commit()
    conn.close()
    if new_badges:
        print("New badges awarded:")
        for name, tier in new_badges:
            print(f"  - {name} ({tier})")
    else:
        print("No new badges earned yet.")


def html_report(student_id: int = None):
    """Generate a simple HTML report for one student or the whole class."""
    conn = get_db()
    cursor = conn.cursor()

    if student_id is not None:
        cursor.execute(
            "SELECT * FROM students WHERE id = ?", (student_id,)
        )
        student = cursor.fetchone()
        if not student:
            print(f"Student {student_id} not found.")
            return 1
        title = f"Mako Coders Report — {student['full_name']}"
        students = [student]
    else:
        title = "Mako Coders Class Report"
        cursor.execute("SELECT * FROM students ORDER BY full_name")
        students = cursor.fetchall()

    lines = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '  <meta charset="UTF-8">',
        f"  <title>{title}</title>",
        "  <style>",
        "    body { font-family: system-ui, sans-serif; max-width: 900px; margin: 2rem auto; }",
        "    table { border-collapse: collapse; width: 100%; margin-bottom: 2rem; }",
        "    th, td { border: 1px solid #ccc; padding: 0.5rem; text-align: left; }",
        "    th { background: #0077b6; color: white; }",
        "    .badge { display: inline-block; background: #caf0f8; padding: 0.25rem 0.5rem; margin: 0.2rem; border-radius: 0.25rem; }",
        "  </style>",
        "</head>",
        "<body>",
        f"  <h1>{title}</h1>",
    ]

    for student in students:
        sid = student["id"]
        cursor.execute(
            "SELECT week_number, band, notes FROM progress WHERE student_id = ? ORDER BY week_number",
            (sid,),
        )
        prog_rows = cursor.fetchall()
        cursor.execute(
            "SELECT badge_name, tier FROM badges WHERE student_id = ? ORDER BY tier, badge_name",
            (sid,),
        )
        badge_rows = cursor.fetchall()

        lines.append(f"  <h2>{student['full_name']} (Grade {student['grade']})</h2>")
        lines.append("  <table>")
        lines.append("    <tr><th>Week</th><th>Module</th><th>Band</th><th>Notes</th></tr>")
        for row in prog_rows:
            module = next((m for m in MODULES if m[0] == row["week_number"]), None)
            module_title = module[2] if module else "Unknown"
            lines.append(
                f"    <tr><td>{row['week_number']}</td><td>{module_title}</td>"
                f"<td>{row['band']}</td><td>{row['notes'] or ''}</td></tr>"
            )
        lines.append("  </table>")

        if badge_rows:
            lines.append("  <h3>Badges</h3>")
            for b in badge_rows:
                lines.append(
                    f"    <span class='badge'>{b['badge_name']} ({b['tier']})</span>"
                )
            lines.append("  <br><br>")

    lines.append("</body>")
    lines.append("</html>")
    conn.close()

    html = "\n".join(lines)
    out_path = ROOT / "tracker" / "report.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"Report written to {out_path}")
    return 0


def main():
    """Parse arguments and dispatch to the right function."""
    parser = argparse.ArgumentParser(description="Mako Coders progress tracker")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("init", help="Create the SQLite database")
    p_add = sub.add_parser("add-student", help="Add a student")
    p_add.add_argument("name")
    p_add.add_argument("grade")

    p_record = sub.add_parser("record", help="Record progress for a student")
    p_record.add_argument("student_id", type=int)
    p_record.add_argument("week", type=int)
    p_record.add_argument("band")
    p_record.add_argument("--notes", default="")

    p_badges = sub.add_parser("badges", help="Recompute badges for a student")
    p_badges.add_argument("student_id", type=int)

    p_report = sub.add_parser("report", help="Generate HTML report")
    p_report.add_argument("--student", type=int, default=None)
    p_report.add_argument("--class", dest="class_report", action="store_true")

    args = parser.parse_args()

    if args.command == "init":
        init_db()
        return 0
    if args.command == "add-student":
        add_student(args.name, args.grade)
        return 0
    if args.command == "record":
        return record_progress(args.student_id, args.week, args.band, args.notes)
    if args.command == "badges":
        award_badges(args.student_id)
        return 0
    if args.command == "report":
        return html_report(student_id=args.student)

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
