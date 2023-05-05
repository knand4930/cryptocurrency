# import subprocess
# from celery import shared_task, Task
# @shared_task
# def run_program(program_path):
#     subprocess.run(program_path, shell=True)
# programs = [
#  "bitcoinfetch.py"
# ]
# for program_path in programs:
#     run_program.delay(program_path)


from tasks import run_program

programs = [
    'seeds/main.py',
    'seeds/mainseeds.py',
]

for program_path in programs:
    print("it is working")
    run_program.delay(program_path)
