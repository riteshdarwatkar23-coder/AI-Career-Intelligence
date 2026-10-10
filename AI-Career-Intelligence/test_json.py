import json

with open("data/jobs.json", "r") as file:
    jobs = json.load(file)

print(jobs)