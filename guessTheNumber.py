import random
secretNumber = random.randint(1, 20)
for guessesTaken in range(7):
    print('Take a guess.')
    guessNumber = int(input())
    if guessNumber < secretNumber:
        print('Your guess is too low.')
    elif guessNumber > secretNumber:
        print('Your guess is too high.')
    else:
        break
if guessNumber == secretNumber:
        print('good job! Your guessed my number in ' + str(guessesTaken + 1) + 'times')
else:
    print('Nope')
