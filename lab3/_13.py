from random import randint as meow


def solve(guess, target, attempts):
    if guess == target:
        return f"Good job, you guessed my number in {attempts} guesses!"
    elif guess < target:
        return "Your guess is too low."
    else:
        return "Your guess is too high."

r = meow(1, 20)
attempts = 0

name = input("Hello! What is your name? ")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")

while 1:
    try:
        guess = int(input("Take a guess. "))
        attempts += 1
        result = solve(guess, r, attempts)
        print(result)
        if guess == r:
            break
    except Exception as ex:
        print(f"Please enter a valid integer. {ex=}")
