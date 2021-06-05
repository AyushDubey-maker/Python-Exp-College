import random

def game(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='p':
            return False
        elif you=='s':
            return True
        elif you=='pe':
            return False
    elif comp=='p':
        if you=='s':
            return False
        elif you=='r':
            return True
        elif you=='pe':
            return True
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True
        elif you=='pe':
            return False
    elif comp=='pe':
        if you=='p':
            return False
        elif you=='r':
            return True
        elif you=='s':
            return False
        




print("Computer's Turn:Rock(r) Paper(p) Scissor(s) Pencil(pe)?")

randNo=random.randint(1,4)

if randNo== 1:
    comp="r"
if randNo==2:
    comp="p"
if randNo==3:
    comp="s"
if randNo==4:
    comp="pe"

you=input("Your Turn:Choose Rock(r) Paper(p) Scissor(s) Pencil(pe)?")

a=game(comp,you)

print(f"Computer chose:{comp}")
print(f"You chose:{you}")
if a == None:
    print("The game is a tie")
elif a:
    print("You win!")
else:
    print("You Loose!")
    
    
    
--------------------------------------------------x-------------------------------------------------x-----------------------------------------
Output:
Computer's Turn:Rock(r) Paper(p) Scissor(s) Pencil(pe)?
Your Turn:Choose Rock(r) Paper(p) Scissor(s) Pencil(pe)?p
Computer chose:r
You chose:p     
You Loose!    
