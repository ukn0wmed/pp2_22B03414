import random

random_number = random.randint(1, 20)

print("Hello! What is your name?")
name = input()

print("Well, {}, I am thinking of a number between 1 and 20.".format(name))
print("Take a guess.")
guess = input()

attempts = 1
guessed = False
while not guessed:
    if int(guess) == random_number:
        print("Good job, {}! You guessed my number in {} guesses!".format(name, attempts))
        guessed = True
    elif int(guess) > random_number:
        print("Your guess is too high.")
        attempts += 1
        print("Take a guess")
        guess = input()
    elif int(guess) < random_number:
        print("Your guess is too low.")
        attempts += 1
        print("Take a guess")
        guess = input()
