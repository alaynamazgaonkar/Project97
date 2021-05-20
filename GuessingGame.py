import random

game=0

num = random.randint(1, 9)

print('Guessing Game')
print("You'll get 5 chances to guess the correct number")
print(' ')

guess1=int(input('Enter your guess :- '))
print(' ')
if guess1>num:
    print('Your guess was too high.')
elif guess1<num:
    print('Your guess was too low.')  
elif guess1==num:
    game=1

if game==0:
    guess2=int(input('Enter your guess :- '))
    print(' ')
    if guess2>num:
        print('Your guess was too high.')
    elif guess2<num:
        print('Your guess was too low.')  
    elif gues2s==num:
        game=1    


if game==0:
    guess3=int(input('Enter your guess :- '))
    print(' ')
    if guess3>num:
        print('Your guess was too high.')
    elif guess3<num:
        print('Your guess was too low.')  
    elif guess3==num:
        game=1


if game==0:
    guess4=int(input('Enter your guess :- '))
    print(' ')
    if guess4>num:
        print('Your guess was too high.')
    elif guess4<num:
        print('Your guess was too low.')  
    elif guess4==num:
        game=1


if game==0:
    guess5=int(input('Enter your guess :- '))
    print(' ')
    if guess5>num:
        print('Your guess was too high.')
    elif guess5<num:
        print('Your guess was too low.')  
    elif guess5==num:
        game=1    


if game==1:
    print('You have won. Congrats!')    

if game==0:
    print('You have lost.')
