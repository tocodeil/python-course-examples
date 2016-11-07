""" read hostname into a python
variable and print it to the user
"""

import subprocess

proc = subprocess.Popen(['/bin/hostname'], stdout=subprocess.PIPE)
(stdout, stderr) = proc.communicate()

print "Hostname = %s" % stdout.strip()
