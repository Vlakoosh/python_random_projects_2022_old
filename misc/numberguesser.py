import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, the number is too low")
        elif guess > random_number:
            print("Sorry, the number is too high")
    print(f"Congrats you have guessed the number {x} correctly")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (h), too low (l), or correct?(c) > ")
        if feedback.lower() == "l":
            low = guess + 1
        elif feedback.lower() == "h":
            high = guess - 1
    print(f"I have guessed the number {guess} correctly!")

computer_guess(20)