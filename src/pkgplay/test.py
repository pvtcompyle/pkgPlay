from datetime import datetime

# input name, birthday, and gender
name = input("Enter your name: ")
birthday = input("Enter your birthday (format: dd-mm-yyyy): ")
gender = input("Enter your gender (male/female): ")

# use the birthday to calculate age
birthday = datetime.strptime(birthday, "%d-%m-%Y")
age = datetime.now().year - birthday.year

# output age using gender appropriate title and name
title = "Mr." if gender.lower() == "male" else "Ms."
print(f"{title} {name}, you are {age} years old.")