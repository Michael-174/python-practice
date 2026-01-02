import random
a = random.randint(1,10)
answer = int(input("please guess a number between 1 and 10"))
attempts = 1
while a != answer:
    if a > answer:
        print("Too small")
        answer = int(input("please guess a number between 1 and 10 again"))
    elif a < answer:
        print("Too big")
        answer = int(input("please guess a number between 1 and 10 again"))
    attempts += 1
print("you are right!")
print("You guessed it in " + attempts + " attempts")