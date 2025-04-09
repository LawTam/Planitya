# trainOS.py
import requests
import sqlite3
import streamlit as st

# Data Ingestion
def fetch_whoop_data(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://api.prod.whoop.com/developer/v1/recovery", headers=headers)
    return response.json()

# Data Storage
def save_to_db(data):
    conn = sqlite3.connect("planitya.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS recovery (date TEXT, score REAL)")
    cursor.execute("INSERT INTO recovery VALUES (?, ?)", ("2025-04-08", data["score"]))
    conn.commit()
    conn.close()

# Workout Logic
def suggest_workout(recovery_score, day):
    split = {"Monday": "Upper", "Tuesday": "Lower", "Wednesday": "Rest"}
    base_workout = split.get(day, "Rest")
    alternatives = ["Running", "Calisthenics", "Gymnastics"]
    if recovery_score > 66:
        return f"Intense {base_workout}", alternatives
    elif recovery_score > 33:
        return f"Moderate {base_workout}", alternatives
    else:
        return "Rest", alternatives

# Dashboard
def run_dashboard():
    st.title("Planitya")
    recovery = 75  # Replace with DB query later
    workout, alts = suggest_workout(recovery, "Monday")
    st.write(f"Recovery: {recovery}%")
    st.write(f"Suggested Workout: {workout}")
    st.write(f"Alternatives: {', '.join(alts)}")

if __name__ == "__main__":
    run_dashboard()