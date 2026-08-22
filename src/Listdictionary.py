# 1. Working with a List
skills_to_learn = ["Python Basics", "Web APIs", "Google GenAI SDK"]

# Add a new skill to the end of the list
skills_to_learn.append("Google Tasks API")

print("--- MY SKILL ROADMAP ---")
print(f"First skill: {skills_to_learn[0]}")  # Lists are 0-indexed!
print(f"Total skills: {len(skills_to_learn)}\n")

# 2. Working with a Dictionary
student_profile = {
    "name": "Durgaprasanti",
    "target_role": "AI Automation Specialist",
    "completed_lessons": 2,
    "is_active": True
}

print("--- STUDENT PROFILE ---")
print(f"Student: {student_profile['name']}")
print(f"Goal: {student_profile['target_role']}\n")

# 3. Combining them: A List of Dictionaries (How APIs return data!)
projects = [
    {"name": "Expense Tracker", "month": 1, "status": "In Progress"},
    {"name": "Daily Summary Bot", "month": 2, "status": "Planned"},
    {"name": "AI Document Summarizer", "month": 3, "status": "Planned"}
]

print("--- PROJECT LIST ---")
# Looping through each item in the list
for project in projects:
    print(f"Month {project['month']}: {project['name']} [{project['status']}]")