""" create a new file named info.txt in current working
directory and then call "rm info.txt" to delete it.
If you're running this on Windows you'll need to replace
subprocess.call line with a one that calls del instead:
    res = subprocess.call(['del', 'info.txt'])
"""

import subprocess

with open('info.txt', 'a'):
    pass

res = subprocess.call(['rm', 'info.txt'])
print "File deleted. Status = %d" % res
