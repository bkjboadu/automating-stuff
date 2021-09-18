import random
import time

import pyinputplus as pyip
numberOfQuestions = 10
correctanswer = 0

for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)


    prompt = f'{questionNumber + 1}: {num1} * {num2} = '
    try:
        answer = pyip.inputNum(prompt,allowRegexes=['%s' % (num1 * num2)],blockRegexes=[('.*','Incorrect!')],timeout=8,limit=3)
    except pyip.TimeoutException:
        print('Out of time')
    except pyip.RetryLimitException:
        print('Out of chances')
    else:
        correctanswer += 1
    time.sleep(2)

print(f'Scores: {correctanswer} / {numberOfQuestions}')