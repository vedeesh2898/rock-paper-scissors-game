import random
user_input=input("rock,paper or scissors")
com_choice= random.choice(['rock','paper','scissors'])
print("You chose:",user_input)
print("computer chose:",com_choice)
if com_choice==user_input:
    print("Its a tie")
elif user_input=="rock":
    if com_choice=='paper':
        print("Computer win")
    else:
        print("You win")
elif user_input=="paper":
    if com_choice=='scissors':
        print("Computer wins")
    else:
        print("you win")
elif user_input=="scissors":
    if com_choice=='rock':
        print("Computer wins")
    else:
        print("you win")






