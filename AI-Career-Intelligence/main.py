import json
import os

profile_path = "student_profile/student_data.json"

def save_profile(profile):
    with open(profile_path, "w") as file:
        json.dump(profile, file, indent=4)

def load_profile():
    try:
        with open(profile_path, "r") as file:
            return json.load(file)
    except:
        print("Could not load the profile.")
        return None
if os.path.exists(profile_path):
    print("Profile already exist.")
    loaded_profile = load_profile()
    if loaded_profile is not None:
        student_profile = loaded_profile
    else:
        print("Profile couldn't be loaded.")
        exit()
        
else:
    print("No profile found.")
    name = input("Enter your name: ")
    branch = input("Enter your branch: ")
    city = input("Enter your city: ")
    target_role = input("Enter your target role: ")
    graduation_year = input("Enter your graduation year: ")
    study_hours = input("How many hours you can study per day?: ")
    skills = [skill.strip() for skill in input("Enter your skills, seperated by commas: ").split(",")]
    student_profile = {
        "name": name,
        "branch": branch,
        "city": city,
        "target_role": target_role,
        "graduation_year": graduation_year,
        "study_hours": study_hours,
        "skills": skills
    }

    save_profile(student_profile)

print("Your name is :", student_profile["name"])
print("Your branch is :", student_profile["branch"])
print("Your city is :", student_profile["city"])
print("Your target role is:", student_profile["target_role"])
print("Your graduation year is:", student_profile["graduation_year"])
print("Your study hours per day:", student_profile["study_hours"])
print("Your skills are:", student_profile["skills"])

print("\n --- Student Profile ---")
print("Name: ", student_profile["name"])
print("Branch: ", student_profile["branch"])
print("City: ", student_profile["city"])
print("Target role: ", student_profile["target_role"])
print("Graduation year: ", student_profile["graduation_year"])
print("Study hours: ", student_profile["study_hours"])
print("Skills: ", student_profile["skills"])


