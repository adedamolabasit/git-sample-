import random
exams_qus=["what colour are banana\n(a)brown\n(b)yellow\n(c)black\n(d)orange\n\n","what colour are snows\n(a)white\n(b)black\n(c)red\n(d)red\n\n", "what is the name of nigeria president\n(a)akinpelu adedamola\n(b)dada temitola\n(c)ibitu michael\n(d)muhammed buhari\n\n "]
class Questions:
    def __init__(questions, question, answer):
        questions.question=question
        questions.answer=answer

questions=[Questions(exams_qus[0],'b'),
           Questions(exams_qus[1],'a'),
           Questions(exams_qus[2],'d')]

def exam(questions):
    score=0
    for qus in questions:
        answer=input(qus.question)
        if answer==qus.answer:
            score+=1
        percentage = round((score / len(questions)) * 100)
        if percentage==50:
            print('average result')
        elif percentage>=60 and percentage<70:
            print('good result')
        elif percentage>70:
            print('excellent')
        else:
            print('you are a failure')

    print(f'you got a total score of {score}/{len(questions)} \n{percentage}%')


exam(questions)




