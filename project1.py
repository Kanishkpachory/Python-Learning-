'''
rovk 1
paper -1
scissor 0

'''
import random
computer = random.choice([1,0,-1])
you = input("enter the choice form Rock-r , paper - p , scisssor - s:  ")
youdict = {"r": 1 , "p": -1 , "s": 0}
revdict = {1:"rock" , -1:"paper" , 0:"scissor"}

make = youdict[you]

print(f"You chose {revdict[make]} \n Computer chose {revdict[computer]}\n")

if (computer == you):
    print("Its a draw try again ! .")
else :
    if(computer == -1 and make == 1):
        print("you loss")
    elif(computer == -1 and make == 0):
        print("you win")
    elif(computer == 1 and make == -1):
        print("you win")
    elif(computer == 1 and make == 0):
        print("you loss")
    elif(computer == 0 and make == 1):
        print("you win") 
    elif(computer == 0 and make == -1):
        print("you loss")
    else:
        print("something went wrong .") 
    