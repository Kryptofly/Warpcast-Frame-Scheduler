from flask import Flask, request, render_template, redirect, url_for, flash
from scheduler.scheduler import add_schedule, get_schedules, remove_schedule
from scheduler.poster import post_frame
import os
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.secret_key = os.urandom(24)
scheduler = BackgroundScheduler()
scheduler.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if request.method == 'POST':
        frame_url = request.form['frame_url']
        post_time = request.form['post_time']
        add_schedule(scheduler, frame_url, post_time)
        flash('Frame scheduled successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('schedule.html')

@app.route('/dashboard')
def dashboard():
    schedules = get_schedules()
    return render_template('dashboard.html', schedules=schedules)

@app.route('/delete/<job_id>')
def delete_schedule(job_id):
    remove_schedule(scheduler, job_id)
    flash('Scheduled frame deleted successfully!', 'success')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
