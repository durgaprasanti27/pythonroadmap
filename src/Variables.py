# 1. Storing data in variables
user_name = "Durgaprasanti"
target_months = 3
hours_per_week = 10.5
is_committed = True

# 2. Doing math with variables
total_hours = target_months * 4 * hours_per_week

# 3. Output using f-strings (formatted strings)
print(f"User: {user_name}")
print(f"Goal: Complete program in {target_months} months.")
print(f"Total estimated study time: {total_hours} hours.")
print(f"Ready to learn: {is_committed}")

# 4. Interactive Input Practice
user_hours = float(input("\nHow many hours can you study this week? "))
weeks_needed = total_hours / user_hours
print(f"At {user_hours} hours/week, it will take you {weeks_needed:.1f} weeks!")