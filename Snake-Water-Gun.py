import random

def game(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you =="w":
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you =="g":
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you =="s":
            return False
        elif you == 'w':
            return True 

matches=int(input("How many matches you want to play? "))

print("Comp Turn :Snake(s) Water(w) Gun(g)?")
randNo=random.randint(1,3)
if randNo== 1:
    comp= "s"
elif randNo == 2:
    comp="w"
elif randNo == 3:
    comp='g'

compPoints=0
userPoints=0

while(matches!=0):

    you=str(input("Player's Turn :Snake(s) Water(w) Gun(g)?")).lower()

    a=game(comp,you)

    print(f"Computer chose:{comp}")
    print(f"You chose:{you}")
    if a == None:
        print("The game is a tie")
        matches-=1
    elif a:
        print("You win!")
        userPoints+=1
        matches-=1
    else:
        print("You Loose!")
        compPoints+=1
        matches-=1

print("Your points: ",userPoints)
print("Computer points: ",compPoints)

if userPoints>compPoints:
    print("Hurray!You won..")
elif userPoints==compPoints:
    print("Match Draw.")
else:
    print("You Loose..")
    
------------------------------------x------------------------------------x----------------------------------------x----------------------------------

Output:
    
How many matches you want to play? 1
Comp Turn :Snake(s) Water(w) Gun(g)?    
Player's Turn :Snake(s) Water(w) Gun(g)?g
Computer chose:w
You chose:g     
You Loose!      
Your points:  0 
Computer points:  1
You Loose..
 
