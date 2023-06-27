from flask import Flask, redirect, url_for, render_template, sessions
from models import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logout')
def logout():
    pass

@app.route('/register')
def register():
    pass

@app.route('/student/dashboard')
def student_dashboard():
    pass

@app.route('/student/settings')
def student_settings():
    pass

@app.route('/student/view/assignments')
def student_view_assignments():
    pass

@app.route('/student/events/calendar')
def student_calendar():
    pass

@app.route('/student/events/reminders')
def student_event_reminders():
    pass

@app.route('/professor/dashboard')
def professor_dashboard():
    pass

@app.route('/professor/view/assignments')
def professor_view_assignments():
    pass

@app.route('/professor/settings')
def professor_settings():
    pass

@app.route('/professor/events/calendar')
def professor_calendar():
    pass

@app.route('/professor/events/reminders')
def professor_event_reminders():
    pass

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404 - Page not found')

if __name__ == '__main__':
    app.run()