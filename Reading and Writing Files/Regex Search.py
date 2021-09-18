import re,os
from pathlib import Path

find = re.compile(r'and')
for file in Path.cwd().glob('*.txt'):
    with open(file,'r') as f:
        if find.search(f.read()):
            print(file)


