import os
import sys
import subprocess


branch = os.environ.get('TRAVIS_PULL_REQUEST_BRANCH', '')
if branch == '':
    sys.exit(0)


runner_path = os.path.dirname(os.path.realpath(__file__))

if not os.path.isfile(os.path.join(runner_path, branch, 'spec.py')):
    sys.exit(0)

res = subprocess.call(
        [sys.executable, 'spec.py'],
        cwd=os.path.join(runner_path, branch))

sys.exit(res)
