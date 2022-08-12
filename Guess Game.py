#Here We are goin to design a game where the User is goin to guess the Index position of a item in the list

#Initial List
mylist=[' ', 'O', ' ']

# Shuffled list
import random

def shuffled_list(mylist):
    mylist=random.shuffle(mylist)
    return mylist

#User's guess

def user_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess = input("Enter your guess i.e. 0,1 or 2")
    return int(guess)

#Checking the users guess is right or wrong
def check_guess(list,guess):
    if mylist[guess]=='O':
        print('Your Guess is Correct')

    else:
        print('Your Guess is wrong')


#Calling functions sequentially

#Initial List
mylist = ['1', '0', '2']

#Shuffled List
mixed_list = shuffled_list(mylist)
print(mixed_list)

#User_guess
#guess = user_guess()

#guess Check
#check_guess(mixed_list, guess)






