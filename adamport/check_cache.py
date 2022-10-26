#!/usr/bin/python3

import subprocess

restart_gunicorn = subprocess.run(["sudo systemctl restart gunicorn"], shell=True)

print("STDOUT: ", restart_gunicorn.stdout)
print("STDERR: ", restart_gunicorn.stderr)

