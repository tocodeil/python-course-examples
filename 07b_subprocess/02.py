import subprocess
import os

subprocess.call(['ls'], cwd=os.path.dirname(__file__))
