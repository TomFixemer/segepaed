from __future__ import print_function
from latex import _unlatex
import codecs
from sys import argv
print(argv[1])
bib = codecs.open(argv[1], 'r', 'utf-8').read()
out = list(_unlatex(bib))
print(len(out))
with codecs.open(argv[1][:-4]+'-normalized.bib', 'w', 'utf-8') as f:
    for k in out:
        try:
            f.write(unicode(k))
        except:
            print(repr(k))
            raw_input()
