from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError
from scheduler.poster import post_frame
from datetime import datetime

def add_schedule(scheduler: BackgroundScheduler, frame_url: str, post_time: str):
    post_time = datetime.strptime(post_time, '%Y-%m-%d %H:%M:%S')
    scheduler.add_job(post_frame, 'date', run_date=post_time, args=[frame_url])

def get_schedules():
    jobs = []
    for job in scheduler.get_jobs():
        jobs.append({
            'id': job.id,
            'frame_url': job.args[0],
            'post_time': job.trigger.run_date.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jobs

def remove_schedule(scheduler: BackgroundScheduler, job_id: str):
    try:
        scheduler.remove_job(job_id)
    except JobLookupError:
        pass
