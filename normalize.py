from __future__ import print_function
from lib.latex import equivalents
from sys import argv
bib = open(argv[1]).read()
for a, b in equivalents.items():
    bib = bib.replace(b, a)
print(len(bib))
with open(argv[1][:-4]+'-normalized.bib', 'w') as f:
    for k in bib:
        try:
            f.write(k)
        except:
            print(repr(k))
            input()
