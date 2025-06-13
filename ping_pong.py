
import random

def ping_pong():
    score = {"Player": 0, "Bot": 0}
    turn = "Player"

    while max(score.values()) < 5:
        if turn == "Player":
            input("Press Enter to hit the ball...")
            hit = random.choice(["In", "Out"])
            print(f"You hit: {hit}")
            if hit == "Out":
                score["Bot"] += 1
        else:
            print("Bot hits the ball...")
            hit = random.choice(["In", "Out"])
            print(f"Bot hit: {hit}")
            if hit == "Out":
                score["Player"] += 1

        print(f"Score -> Player: {score['Player']} | Bot: {score['Bot']}")
        turn = "Bot" if turn == "Player" else "Player"

    winner = max(score, key=score.get)
    print(f"{winner} wins the game!")

if __name__ == "__main__":
    ping_pong()
