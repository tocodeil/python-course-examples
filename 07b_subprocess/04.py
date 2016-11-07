""" reads input numbers as command line arguments,
concatenate them all into one long string with +
between each two numbers and send the string to bc
to get the sum
"""

import sys
import subprocess

proc = subprocess.Popen(
        ['/usr/bin/bc'],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE)

calc = '+'.join(sys.argv[1:])
print 'Calculating: "%s"' % calc

(stdout, stderr) = proc.communicate(calc + "\n")
print "Result = %s" % stdout.strip()
