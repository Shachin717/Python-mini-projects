import random
num=random.randint(1,100)
attempts=0
print("NUmber Guessing game")
print("Guess a number between 1 to 100")

while True :
    s=input()
    if s.lower()=="q":
        print("Game exited. Thanks for playing!")
        break
    if not s.isdigit():
        print("Please enter a valid number")
        continue
    s=int(s)
    attempts+=1
    if s<num:
        print("Too low")
    elif s>num:
        print("Too high")
    else:
        print(f"Number found in {attempts} attempts!")
        break    

