from job_data import load_jobs
from fastapi import APIRouter, Depends, HTTPException
from models import Job


router = APIRouter()

def get_api_message():
    return "AI Career Intelligence API"
@router.get("/message")
def read_message(message: str = Depends(get_api_message)):
    return {"message": message}



@router.get("/jobs", response_model=list[Job])
def get_jobs(location: str | None=None, role: str | None=None):
    jobs = load_jobs()

    filtered_jobs = []

    for job in jobs:
        location_matches = (location is None or location.lower() in job["location"].lower())

        role_matches = (role is None or role.lower() in job["title"].lower())

        if location_matches and role_matches:
            filtered_jobs.append(job)

    return filtered_jobs

