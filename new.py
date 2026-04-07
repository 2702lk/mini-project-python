import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Number Guessing Game")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Enter a valid number!")
            continue

        attempts += 1

        # 🎯 Special feature
        if guess == 7:
            print("🍀 Good Luck!")

        if guess == number:
            print("🎉 Correct!")
            break
        elif guess < number:
            print("Too Low")
        else:
            print("Too High")

    else:
        print("Game Over! Number was:", number)

play_game()