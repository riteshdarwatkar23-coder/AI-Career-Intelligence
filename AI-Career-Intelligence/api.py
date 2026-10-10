import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

class Job(BaseModel):
    title: str = Field(min_length=1)
    company: str = Field(min_length=1)
    location: str = Field(min_length=1)

    @field_validator("title", "company", "location")
    @classmethod
    def reject_whitespace_only(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Feild cannot contain only spaces")
        return value
                            
app = FastAPI()
JOBS_FILE = Path(__file__).parent / "data" / "jobs.json"
def load_jobs():
    with open(JOBS_FILE,"r") as file:
        return json.load(file)

@app.get("/jobs")
def get_jobs(location: str | None=None, role: str | None=None):
    jobs = load_jobs()

    filtered_jobs = []

    for job in jobs:
        location_matches = (location is None or location.lower() in job["location"].lower())

        role_matches = (role is None or role.lower() in job["title"].lower())

        if location_matches and role_matches:
            filtered_jobs.append(job)

    return filtered_jobs

@app.get("/jobs/{job_id}")
def get_job(job_id: int):
    jobs = load_jobs()
    if job_id<0 or job_id>=len(jobs):
        raise HTTPException(
            status_code=404,
            detail= "Job not found"
        )
    return jobs[job_id]

    

@app.post("/jobs",status_code=201)
def create_job(job: Job):
    jobs = load_jobs()

    jobs.append(job.model_dump())

    with open(JOBS_FILE, "w") as file:
        json.dump(jobs, file ,indent = 4)

    return job

