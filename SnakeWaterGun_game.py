i=0
hp=0
cp=0
drw=0
ev=0
while (i<10):
    import random
    lst= ["Snake","Water","Gun"]
    b= random.choice(lst)
    i=i+1
    print("Press\n 1 for Snake\n 2 for Water\n 3 for Gun") 
    x1=int(input(""))       
    if b== ("Snake") and x1== (2):
        print ("You Won!")
        print("Chances left: ",10-i)
        hp=hp+1
    elif b== ("Snake") and x1== (3):
        print ("You Lose!")
        print("Chances left: ",10-i)
        cp=cp+1
    elif b== ("Snake") and x1== (1):
        print ("Draw!!") 
        drw=drw+1
        print("Chances left: ",10-i)
        cp=cp+0
        hp=hp+0
    elif b== ("Water") and x1== (3):
        print ("You Lose!")  
        print("Chances left: ",10-i)
        cp=cp+1
    elif b== ("Water") and x1== (2):
        print ("Draw!!")
        drw=drw+1
        print("Chances left: ",10-i)
        cp=cp+0
        hp=hp+0
    elif b== ("Gun") and x1== (3):
        print ("Draw!!")  
        drw=drw+1
        print("Chances left: ",10-i)
        cp=cp+0
        hp=hp+0
    elif b== ("Water") and x1== (1):
        print ("You won!")
        print("Chances left: ",10-i)
        hp=hp+1
    elif b== ("Gun") and x1== (1):
        print ("You Lose!")
        print("Chances left: ",10-i)
        cp=cp+1
    elif b== ("Gun") and x1== (2):
        print ("You Won!")
        print("Chances left: ",10-i) 
        hp=hp+1    
    else:
        print("Please enter valid number!!")
        ev=ev+1     
     
print(f"\n\nYour Final Score= {hp}")  
print(f"Computer Final Score= {cp}")   
print(f"Number of draw: {drw}") 
print(f"Entered invalid numbers: {ev}")  
if hp>cp:
    print("Congratulations!! You Won the game")
if cp>hp:
    print("Computer Won the game!")
if cp==hp:
    print("Draw!!!")     
if ev==10:
    print ("All inputs invalid")
