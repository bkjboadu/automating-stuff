import re

def strip(text, remove = " "):
    remove_start = re.compile(r'^[%s]' % remove)
    remove_end = re.compile(r'[%s]$' % remove)
    start = remove_start.findall(text)
    end = remove_end.findall(text)
    return text[len(start):len(text) - len(end)]

utext = input('text:')
ustrip = input('strip:')
print(strip(utext,ustrip))


