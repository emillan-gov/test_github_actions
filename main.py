# src/main.py

import subprocess
import os

def run_subprocess():
    subprocess.run(["python", os.path.join(os.path.dirname(__file__), "subprocess.py")])

if __name__ == "__main__":
    print("Running main script")
    run_subprocess()
