import re,shutil,os
from pathlib import Path

ameriregex = re.compile(r'''(
(\d{,2}) #month
-      #separator
(\d{,2}) #day
-      #separator
(\d{4})  #year
)''',re.VERBOSE)


for file in Path.cwd().glob('*'):
    ams = ameriregex.findall(str(file))
    if len(ams) == 0:
        continue

    for group in ams:
        euro = group[2] + '-' +  group[1] + '-' + group[3]
        new_name = ameriregex.sub(euro,str(file))
    os.rename(file,new_name)


