import re
multi_spaces = re.compile(r'''(
\s{2,} #multiple spacing
)''',re.VERBOSE)

repeated_words = re.compile(r'\b(\w+)\s+\1\b')

multi_exclamation = re.compile(r'''(
!{2,}$
)''')

text = 'Find common typos such as multiple  spaces  between words, accidentally accidentally repeated   words, or multiple exclamation marks at theend of sentences. Those are annoying!!'

all = []
for multispaces in multi_spaces.findall(text):
    all.append(multispaces)

for multiexclamation in multi_exclamation.findall(text):
    all.append(multiexclamation)

for repeatword in repeated_words.findall(text):
    all.append(repeatword)

print(all)