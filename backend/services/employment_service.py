import random

job_statuses = ["unemployed", "informal", "formal"]

informal_jobs = ["street_vendor", "driver", "freelancer", "farmer"]
formal_jobs = ["office_staff", "teacher", "engineer", "government_worker"]

def get_employment(citizen_id: str):
    status = random.choices(
        job_statuses,
        weights=[0.2, 0.5, 0.3]  # realistic-ish distribution
    )[0]

    if status == "unemployed":
        job = "none"
        income = random.randint(0, 2)

    elif status == "informal":
        job = random.choice(informal_jobs)
        income = random.randint(1, 5)

    else:
        job = random.choice(formal_jobs)
        income = random.randint(4, 10)

    return {
        "job_status": status,
        "job_type": job,
        "income": income
        
    }