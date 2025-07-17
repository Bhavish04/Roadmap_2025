import random
number=random.randint(1,100)
attempt=0
while True:
    guess=int(input("Guess the number (1-100)"))
    attempt+=1
    if guess>number:
        print("Too High")
    elif guess<number:
        print("Too Low")
    else:
        print(f"Congratulation you guessed the number correct in {attempt} tries")
        break