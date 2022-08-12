list=[' ', 'O', ' ']
# Shuffled list
import random

def shuffled_list(list):
    list = random.shuffle(list)
    return list

mylist=['0', '1', '2']
shuffled_list(mylist)
print(mylist)

#User's guess

def user_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Enter your guess i.e. 0,1 or 2")
    return int(guess)

#Checking the users guess is right or wrong
def check_guess(list,guess):
    if mylist[guess]=='O':
        print('Your Guess is Correct')

    else:
        print('Your Guess is wrong')

tlist=['0', '1', '2']
shuffled_list(tlist)
user_guess()
check_guess(tlist,guess)