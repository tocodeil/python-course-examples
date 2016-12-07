import sys
#print sys.argv[1:]


pc_list = set(sys.argv[1:])
dictionary = {}

with open(r"C:\Temp\Hosts", "r") as rows:
    for row in rows:
        dictionary.setdefault(row.split("=")[0], row.split("=")[1].strip('\n'))

#print dictionary

for pc in pc_list:
    print "%s ==> %s" % (pc, dictionary.get(pc, 'PC was not identified in hosts file'))
