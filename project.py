from random import randint

player = randint(1,6)
computer = randint(1,6)
count1 = 0        #player
count2 = 0        #computer

round = 1
while(round < 4):
    print("roll %s" %(str(round)))
    print("you rolled", player)
    print("computer rolled", computer)
    count1 = count1 + player
    count2 = count2 + computer
    player = randint(1,6)
    computer = randint(1,6)
    round = round + 1
    
if(count1 > count2):
    print("You won!")
elif(count1 < count2): 
    print("You lost.")
elif(count1 == count2):    
    print("You tied.")