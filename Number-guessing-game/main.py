import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Number Guessing Game")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number:
            print("Correct!")
            break
        elif guess < number:
            print("Too Low")
        else:
            print("Too High")

    else:
        print("Game Over! Number was:", number)

play_game()