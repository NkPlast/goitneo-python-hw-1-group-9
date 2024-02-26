from datetime import datetime, timedelta
from collections import defaultdict

today = datetime.now().date()
monday_of_this_week = today - timedelta(days=today.weekday())
monday_of_next_week = monday_of_this_week + timedelta(days=7)
sunday_of_next_week = monday_of_next_week + timedelta(days=6)

def get_birthdays_per_week(users):
    birthdays = defaultdict(list)
    for user in users:
        
        birthday_this_year = user["birthday"].replace(year=today.year)
        
        if monday_of_next_week <= birthday_this_year.date() <= sunday_of_next_week:
            weekday = birthday_this_year.strftime("%A")
            birthdays[weekday].append(user["name"])
        
        elif birthday_this_year.weekday() >= 5:
            birthdays["Monday"].append(user["name"])

    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")

# Пример списка пользователей
users = [
    {"name": "John Doe", "birthday": datetime(1984, 2, 29)},
    {"name": "Jane Doe", "birthday": datetime(1990, 2, 28)},
    {"name": "Alice Cooper", "birthday": datetime(1978, 3, 1)},
    {"name": "Bob Marley", "birthday": datetime(1945, 2, 6)},
]


get_birthdays_per_week(users)
