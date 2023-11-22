import random

def roll_die():
    return random.randint(1, 6)

def dice_rolling_simulator():
    score=0
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        input("Press Enter to roll the die...")

        result = roll_die()
        print(f"You rolled: {result}")
        score=score+result

        play_again = input("Roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("score:",score)
            print("Thanks for rolling! Goodbye.")
            break


dice_rolling_simulator()
