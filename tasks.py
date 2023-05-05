import subprocess
from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def run_program(program_path):
    subprocess.run(program_path, shell=True)
