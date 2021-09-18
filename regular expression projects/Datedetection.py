import datetime
import re
import pyperclip


date_detect = re.compile(r'''(
(\d{2}) #day
/
(\d{2}) #month
/
(\d{4}) #year
)''',re.VERBOSE)

text = str(pyperclip.paste())
if len(text) == 0:
    text = '''
    Write a regular expression that can detect dates in the DD/MM/YYYY format.
    Assume that the days range from 01 to 31, the months range from 01
    to 12, and the years range from 1000 to 2999. Note that if the day or month
    is a single digit, it’ll have a leading zero.
    The regular expression doesn’t have to detect correct days for each
    month or for leap years; it will accept nonexistent dates like 31/02/2020 or
    31/04/2021. Then store these strings into variables named month, day, and
    year, and write additional code that can detect if it is a valid date. April,
    June, September, 22/02/1999 and November have 30 days, February has 28 days, and
    the rest of the months 13/04/2021 have 31 days. February has 29 days in 12/12/2050 leap years.
    Leap years are every year evenly divisible by 4, except for years evenly divisible
    by 100, unless the year is also evenly divisible 13/02/2021 by 400. Note how this calculation
    makes it impossible to make a reasonably sized regular expression
    that can detect a valid date.
    '''


valid_date = []
invalid_date = []
for date in date_detect.findall(text):
    day = int(date[1])
    month = int(date[2])
    year = int(date[3])
    try:
        if datetime.datetime(year,month,day):
            valid_date.append(date[0])
    except ValueError:
        invalid_date.append(date[0])

print(valid_date)
print(invalid_date)

