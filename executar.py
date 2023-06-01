import subprocess
import os

venv_path = r'venv'
python_executable = os.path.join(venv_path, 'Scripts', 'python.exe')
server_script = os.path.join('src', 'backEnd', 'server.py')

subprocess.run([python_executable, server_script])
