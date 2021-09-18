import re

import pyperclip

dateregex = re.compile(r'''(
(\d+) #day
(/|-)
(\d+) #month
(/|-)
(\d+)) #year
''',re.VERBOSE)

text = 'Clean up dates in different date formats (such as 3/14/2019, 03-14-2019,and 2015/3/19) by replacing them with dates in a single, standard format'

match = []

for date in dateregex.findall(text):
    match.append(date)

print(match)



for date in match:
    #declaring day,month and year
    if 12 >= int(date[1]) >= 1 and int(date[3]) < 32:
        month = date[1]
        day = date[3]
        year = date[5]
    elif int(date[1]) > 31 and int(date[3]) < 13 and int(date[5]) < 13:
        year = date[1]
        month = date[3]
        day = date[5]
    elif int(date[1]) > 31 and int(date[5]) > 12:
        year = date[1]
        month = date[3]
        day = date[5]
    elif int(date[1]) > 31 and int(date[3]) > 12:
        year = date[1]
        day = date[3]
        month = date[5]

    standard = day + '/' + month + '/' + year
    newdateregex = re.compile(date[0])
    replace = newdateregex.sub(standard,text)
    text = replace


print(replace)






