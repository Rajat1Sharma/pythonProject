import os
def user_choice(choice):

#digit check
    choice = "Wrong"
    while choice.isdigit() == False:
        choice = input("Enter the desired number range in between (0-10)")
        if choice.isdigit()==False:
            print("The entered value is not digit please enter again")
            break
        acceptable_value = range(0, 10)
        if choice not in acceptable_value:
               print("The entered no. is not in the range(0-10)")

    print(int(choice))


user_choice(0)


for num in range(0,101):
    os.system(f"touch file_{num}")








