import re,os
from pathlib import Path

spamregex = re.compile(r'(spam(\d{2})\.txt)')

path = os.getcwd()
match = []
for files in os.listdir(path):
    if not spamregex.findall(files):
        continue
    match.append(spamregex.findall(files)[0])

print(match)
new_name = [match[0]]

for i in range(len(match)-1):
    if int(new_name[i][1]) != int(match[i+1][1]) - 1:
        new_name.append(('spam' + str(int(new_name[i][1])+1) + '.txt',str(int(new_name[i][1])+1)))
    else:
        new_name.append(match[i+1])

for i in range(len(new_name)):
    os.rename(match[i][0],'spam' + str(int(new_name[i][1])) + '.txt')

print(new_name)