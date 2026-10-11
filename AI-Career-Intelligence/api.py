import json
from job_data import load_jobs, JOBS_FILE
from fastapi import FastAPI, HTTPException
from jobs import router as jobs_router
from models import Job
                            
app = FastAPI()
app.include_router(jobs_router)


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


@app.put("/jobs/{job_id}")
def update_job(job_id: int, job: Job):
    jobs = load_jobs()

    if job_id<0 or job_id>=len(jobs):
        raise HTTPException(
            status_code=404,
            detail = "Job not found"
        )
    jobs[job_id] = job.model_dump()

    with open(JOBS_FILE,"w") as file:
        json.dump(jobs,file, indent=4)
    return jobs[job_id]

@app.delete("/job/{job_id}")
def delete_job(job_id: int):
    jobs = load_jobs()

    if job_id<0 or job_id>=len(jobs):
        raise HTTPException(
            status_code=404,
            detail= "Job not found"
        )
    deleted_job = jobs.pop(job_id)
    with open(JOBS_FILE,"w") as file:
        json.dump(jobs,file,indent=4)
    return {
        "message": "Job deleted successfully",
        "job": deleted_job
    }