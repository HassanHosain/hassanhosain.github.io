#RANDOM GUESSING number game
import random

def guess(x):
    random_number = random.randint(1,x)#random number between 1 to x
    guess_number=0 #because the random_number is set to 1 to x it will never be 0

    while guess_number != random_number:
        guess_number=int(input(f'Guess a number between 1 and {x}:'))
        
        if guess_number > random_number:
            print('The number is lower then what you guess')
        elif guess_number<random_number:
            print(' The number is higher than what you guessed')
        
    print(f'Congratulations {guess_number} is the correct number. You have guessed correctly!!')

def computer_guess(x):
    low_bound=1
    high_bound=x
    feedback=''
    while feedback != 'c' and low_bound != high_bound:
        if low_bound != high_bound:
            guess = random.randint (low_bound,high_bound)
        else:
            guess=low_bound # could also be high_bound
        #guess= random.randint(low_bound, high_bound)
        feedback=input(f'Is {guess} too high (H), too low(L), or correct (C)?').lower
        if feedback == 'h':
            high_bound = guess - 1
        elif feedback == 'l':
            low_bound = guess + 1
    print(f'Yay! The computer guessed your number, {guess}, correctly!')

computer_guess(10)
  
