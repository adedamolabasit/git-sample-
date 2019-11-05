import random
exams_qus=["what colour are banana\n(a)brown\n(b)yellow\n(c)black\n(d)orange\n\n",
           "what colour are snows\n(a)white\n(b)black\n(c)red\n(d)green\n\n",
           "what is the name of nigeria president\n(a)akinpelu adedamola\n(b)dada temitola\n(c)ibitu michael\n(d)muhammed buhari\n\n "]

class Question:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer
        random.choice(exams_qus)


questions=[Question(exams_qus[0],'b'),
    Question(exams_qus[1],'a'),
    Question(exams_qus[2],'d')]

def cbt_qus(questions):
    score=0
    for item in questions:
        answer=input(item.question)
        if answer==item.answer:
            score+=1
    percentage = round((score / len(questions)) * 100)
    if percentage<50:
        print('failed')
    elif percentage==50:
        print('average')
    elif percentage>50 and percentage<=60:
        print('pass')
    elif percentage>60 and percentage<70:
        print('good')
    else:
            print('excellent')
    print(f'{score}/{len(questions)}')
    print(f'{percentage}%')



exam=cbt_qus(questions)
print(exam)





