def Test(name):
    print(f'Welcome to IST1020 CAT 1')
    print('')
    print('Attemp all questions')
    print('')
    score = 0
    firstAnswer = 'central processing unit'
    secondAnswer = 'althmetic logical unit'
    thirdAnswer = 'monitor'
    fourthAnswer = 'random access memory'
    fifthAnswer = 'read only memory'
    sixthAnswer = 'scanner'
    sevethanswer = ['mouse', 'keyboard', 'screen', 'scanner', 'projector']
    systems = ['Windows', 'MAC 0S', 'Linux']
    course = 'applied computer technology'
    languages = ['Java', 'python', 'JavaScript', 'HTML', 'CSS', 'SQLAlchemy']

    while True:
        
        #identity = int(input('Enter your student ID: '))
        print('')
        n = (input('ready?').lower()).strip()
        if n != 'yes':
            quit()

        else:
            print('')
            q1 = (input('What does CPU stands for? ').lower()).strip()
            if q1 != firstAnswer:
                pass
            else:
                score +=1


            print('')

            q2 = (input('What does ALU stands for? ').lower()).strip()
            if q2 != secondAnswer:
                pass
            else:
                score +=1

            print('')

            q3= (input('Which part of the computer system that displays informarion for the user? ').lower()).strip()
            if q3 != thirdAnswer:
                pass
            else:
                score +=1

            print('')

            q4= (input('What does RAM stands for? ').lower()).strip()
            if q4 != fourthAnswer:
                pass
            else:
                score +=1

            print('')

            q5 = (input('What does ROM stands for? '))
            if q5 != fifthAnswer:
                pass
            else:
                score +=1

            print('')

            q6 = (input('What is the device used to turn hard copy to soft copy? ').lower()).strip()
            if q6 != sixthAnswer:
                pass
            else:
                score +=1

            print('')

            q7 = (input('name one of external devices you know: ').lower()).strip()
            if q7 not in sevethanswer:
                pass
            else:
                score +=1

            print('')

            q8 = (input('Name one operating system you know so far: ').lower()).strip()
            if q8 not in systems:
                pass
            else:
                score +=1

            print('')

            q9 = (input('What does APT stands for: ').lower()).strip()
            if q9 != course:
                pass
            else:
                score +=1

            print('')

            q10 = (input('Tell one of programming languages you know: ').lower()).strip()
            if q10 not in languages:
                pass
            else:
                score +=1

            print('')


            print(f'Thank you {name} for taking the test.')
            print(f'After examining your progrecess we realized you have gottern {score}')


