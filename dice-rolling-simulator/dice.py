import random
while True :
    print("Roll the dice ? (y/n):")
    c=input().lower()
    if c=="y":
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"({die1},{die2})")
    elif c=="n":
        print("Thank you!")
        break
    else:
        print("Invalid") 
    
