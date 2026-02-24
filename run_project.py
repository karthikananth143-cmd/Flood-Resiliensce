import subprocess
import time

subprocess.Popen(["npx", "node-red"], shell=True)
time.sleep(5)
subprocess.Popen(["python", "-m", "streamlit", "run", "app.py"], shell=True)