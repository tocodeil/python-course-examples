""" The stdout parameter of subprocess.call can
take an existing file handle and send all output
to that file. Here's how we use that feature
to open a file and write a cow into it
"""


import subprocess

with open('mycow', 'w') as cowfile:
    subprocess.call(
            ['/usr/local/bin/cowsay', 'Hello Python'],
            stdout=cowfile)
