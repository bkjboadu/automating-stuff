import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka',
'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta',
'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing',
'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City',
'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City',
'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe',
'New York': 'Albany', 'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 'Columbus',
'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville',
'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier',
'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for textNumber in range(35):
    #create questions paper and answerSheet
    quizfile = open(f'Capitalquiz{textNumber + 1}.txt','w')
    ansfile = open(f'Capitalquiz{textNumber + 1}ans.txt','w')

    #write headers on question paper
    quizfile.write(' ' * 20 + f'Pantang Hospital J.H.s\n\n')
    quizfile.write(f'Name:\nClass:\nDate:\nSubject:\n\n')

    for questionNumber in range(50):
        states = list(capitals.keys())
        random.shuffle(states)
        possibleans = list(capitals.values())
        correctAnswer = capitals[states[questionNumber]]
        del possibleans[possibleans.index(correctAnswer)]
        wrongAnswers = random.sample(possibleans,3)
        Answers = wrongAnswers + [correctAnswer]
        random.shuffle(Answers)
        quizfile.write(f'{questionNumber + 1}. What is the Capital City of {states[questionNumber]}?\n')
        for i in range(4):
            quizfile.write(f"{'ABCD'[i]}.{Answers[i]}\n")
        quizfile.write('\n')
        ansfile.write(f"{questionNumber + 1}.{'ABCD'[Answers.index(correctAnswer)]}\n")
    quizfile.close()
    ansfile.close()

