import re,pyperclip
import pyinputplus as pyip

text = '''The ADJECTIVE panda walked to the NOUN and then VERB . A nearby NOUN was
unaffected by these events.'''

word_to_replace = ['ADJECTIVE','NOUN','ADVERB','VERB']


for word in text.split():
    print(word)
    if word not in word_to_replace:
        pass

    regex = re.compile(word, re.I)
    if word == 'ADJECTIVE':
        ADJECTIVE = pyip.inputStr('Enter an adjective:')
        text = regex.sub(ADJECTIVE,text)
    elif word == 'NOUN':
        NOUN = pyip.inputStr('Enter a noun:')
        text = regex.sub(NOUN, text)
    elif word == 'ADVERB':
        ADVERB = pyip.inputStr('Enter a adverb:')
        text = regex.sub(ADVERB, text)
    elif word == 'VERB':
        VERB = pyip.inputStr('Enter a verb:')
        text = regex.sub(VERB, text)
    else:
        continue

print(text)