import random

def setAnswer(a, b):
    answer = random.randint(a,b)
    return answer

def startGame(answer, l, r):
    while True:
        try:
            guess = int(input(f'Enter number between {l} to {r}: '))
            if guess>=1 and guess<11:
                if(guess==answer):
                    print("You got it")
                    break
            else:
                print("provide right input")
        except ValueError as err:
            print("Enter a number")
    return True
