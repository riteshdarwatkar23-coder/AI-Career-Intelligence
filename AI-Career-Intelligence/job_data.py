
import json
from pathlib import Path
from fastapi import HTTPException

JOBS_FILE = Path(__file__).parent / "data" / "jobs.json"


def load_jobs():
    try:
        with open(JOBS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="The jobs data file contains invalid JSON."
        )