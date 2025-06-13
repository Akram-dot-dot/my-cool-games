
import random

def snake_and_ladders():
    position = 0
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    while position < 100:
        input("Press Enter to roll the dice...")
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}")
        position += roll

        if position in snakes:
            print(f"Oh no! Snake bite at {position}")
            position = snakes[position]
        elif position in ladders:
            print(f"Yay! Ladder climb at {position}")
            position = ladders[position]

        print(f"You're now at {position}")

    print("Congratulations! You reached 100 and won!")

if __name__ == "__main__":
    snake_and_ladders()
