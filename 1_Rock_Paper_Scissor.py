import random
import time

def result(u,c):
    user = u.lower()
    comp = c.lower()
    if user == comp:
        return 0
    elif user=='r':
        if comp =='p':
            return -1
        else:
            return 1
    elif user=='p':
        if comp =='s':
            return -1
        else:
            return 1
    elif user=='s':
        if comp =='r':
            return -1
        else:
            return 1
    else:
        print("\nSomething Went Wrong....")

def full(u,c):
    if u=='R':
        if c=='R':
            return 'Rock','Rock'
        elif c=='P':
            return 'Rock', 'Paper'
        else:
            return 'Rock', 'Scissor'
    elif u=='P':
        if c=='R':
            return 'Paper','Rock'
        elif c=='S':
            return 'Paper', 'Scissor'
        else:
            return 'Paper', 'Paper'
    else:
        if c=='R':
            return 'Scissor','Rock'
        elif c=='P':
            return 'Scissor', 'Paper'
        else:
            return 'Scissor', 'Scissor'

user = input("Enter : \n\t(R) for Rock \n\t(P) for Paper \n\t(S) for Scissor\n\tEnter Choice : ")
user = user.upper()
n = random.randint(1,3)
if n==1:
    comp = 'R'
elif n==2:
    comp = 'P'
else:
    comp = 'S'

user_full,comp_full = full(user,comp)

r = result(user,comp)
if r==1:
    data = f"\nUSER : {user_full} > COMPUTER : {comp_full} \nResult of the Match : USER WINS!!!"
elif r==-1:
    data = f"\nUSER : {user_full} < COMPUTER : {comp_full} \nResult of the Match : COMPUTER WINS!!!"
else:
    data = f"\nUSER : {user_full} = COMPUTER : {comp_full} \nResult of the Match : IT'S A DRAW!"

print(data)

with open("1_Record_rock_paper_scissor.txt","a") as f:
    f.write("\n")
    f.write(f"Date : {time.asctime(time.localtime(time.time()))}")
    f.write(data)
    f.write("\n")