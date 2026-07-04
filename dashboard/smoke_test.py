"""
Smoke test the Mako Coders dashboard using Flask's test client.
Run: python3 dashboard/smoke_test.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from app import app, init_db


def main():
    init_db()
    client = app.test_client()

    # Home page loads
    r = client.get("/")
    assert r.status_code == 200, f"Home failed: {r.status_code}"
    assert b"Mako Coders Quiz Dashboard" in r.data, "Home missing title"
    print("✅ Home page loads")

    # Add a student
    r = client.post(
        "/student/add",
        data={"name": "Amina", "age_band": "10-13", "grade": "Grade 7"},
        follow_redirects=True,
    )
    assert r.status_code == 200, f"Add student failed: {r.status_code}"
    print("✅ Student added")

    # Dashboard loads
    r = client.get("/student/1")
    assert r.status_code == 200, f"Dashboard failed: {r.status_code}"
    assert b"Amina" in r.data, "Dashboard missing student name"
    print("✅ Student dashboard loads")

    # Quiz page loads
    r = client.get("/quiz/1/1")
    assert r.status_code == 200, f"Quiz page failed: {r.status_code}"
    assert b"Week 01 Quiz" in r.data or b"Week 1 Quiz" in r.data, "Quiz missing week title"
    print("✅ Quiz page loads")

    # Submit quiz
    quiz_data = {
        "q1": "Competency-Based Education",
        "q2": "Papa",
        "q3": "Do not share passwords",
        "q4": "Save work often",
        "q5": "The trail you leave online",
        "q6": "Being fast",
        "q7": "A project folder",
        "q8": "To work safely",
        "q9": "Believing you can learn",
        "q10": "Sharing information",
    }
    r = client.post("/quiz/1/1", data=quiz_data, follow_redirects=True)
    assert r.status_code == 200, f"Quiz submit failed: {r.status_code}"
    assert b"result" in r.data.lower() or b"%" in r.data, "Result page missing score"
    print("✅ Quiz submitted and scored")

    # Achievements awarded
    r = client.get("/student/1")
    assert b"First Splash" in r.data, "Missing first badge"
    print("✅ Achievement awarded")

    # Print report loads
    r = client.get("/print/1")
    assert r.status_code == 200, f"Print report failed: {r.status_code}"
    assert b"Student Progress Report" in r.data, "Print report missing title"
    print("✅ Printable report loads")

    print("\n🦈 All dashboard smoke tests passed.")


if __name__ == "__main__":
    main()
