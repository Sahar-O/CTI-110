# Sahar Olaya
# 2025-04-20
# P5HW
# Emoji Treasure Hunt Game 🎯💰🔑
# An interactive game with challenges and surprises in multiple rooms.

import random
import time

def create_player():
    """Returns a dictionary containing player's info."""
    name = input("Enter your adventurer name: ")
    return {
        "name": name,
        "score": 0,
        "inventory": []
    }

def room_challenge(room_number, player):
    """Each room presents a different challenge."""
    print(f"\n🚪 Room {room_number} Challenge...")
    time.sleep(1.5)

    if room_number == 1:
        print("🎲 A dice game! Roll higher than 3 to win.")
        input("Press Enter to roll the dice...")
        roll = random.randint(1, 6)
        print(f"You rolled a {roll} 🎲")
        if roll > 3:
            print("🎉 You win 5 points!")
            player["score"] += 5
        else:
            print("😢 You lose 2 points.")
            player["score"] -= 2

    elif room_number == 2:
        print("🧠 What is 7 * 8?")
        print("A. 54")
        print("B. 56")
        print("C. 58")
        print("D. 60")
        choice = input("Your answer (A, B, C, or D): ").strip().upper()
        if choice == "B":
            print("✅ Correct! +10 points.")
            player["score"] += 10
        else:
            print("❌ Incorrect. The correct answer was B. 56")
            player["score"] -= 3

    elif room_number == 3:
        print("🤔 Which of these animals is a mammal?")
        print("A. Eagle")
        print("B. Snake")
        print("C. Dolphin")
        print("D. Turtle")
        choice = input("Your answer (A, B, C, or D): ").strip().upper()
        if choice == "C":
            print("👏 Correct! Dolphins are mammals. +10 points.")
            player["score"] += 10
        else:
            print("🙈 Oops! The correct answer was C. Dolphin.")
            player["score"] -= 3

    elif room_number == 4:
        print("💡 What goes up but never comes down?")
        print("A. Balloon")
        print("B. Smoke")
        print("C. Age")
        print("D. Temperature")
        choice = input("Your answer (A, B, C, or D): ").strip().upper()
        if choice == "C":
            print("🎉 Correct! +10 points.")
            player["score"] += 10
        else:
            print("❌ Nope! The answer was C. Age.")
            player["score"] -= 5

    elif room_number == 5:
        print("🧙‍♂️ A wizard offers you a potion.")
        print("A. Drink it")
        print("B. Refuse it")
        choice = input("Your choice (A or B): ").strip().upper()
        if choice == "A":
            if random.choice([True, False]):
                print("✨ It's a blessing! You gain a key!")
                player["inventory"].append("treasure key")
                player["score"] += 5
            else:
                print("😵‍💫 It was cursed! You lose 5 points.")
                player["score"] -= 5
        else:
            print("You wisely refused the potion.")

    elif room_number == 6:
        print("🚪 You've reached the treasure door!")
        if "treasure key" in player["inventory"] or player["score"] >= 30:
            print("🔑 You unlocked the treasure! 🎉💰")
            player["inventory"].append("treasure")
            player["score"] += 20
        else:
            print("🔒 You don't have the key or enough points. Try again later.")

def main():
    print("🎮 Welcome to the Emoji Treasure Hunt!")

    while True:
        player = create_player()

        for i in range(1, 6):
            room_challenge(i, player)
            time.sleep(1.5)

        print("\n🚪 Final Room 6: Treasure Door...")
        room_challenge(6, player)

        print("\n🏁 Game Over!")
        print(f"Player: {player['name']}")
        print(f"Inventory: {player['inventory']}")
        print(f"Final Score: {player['score']}")

        if "treasure" in player["inventory"]:
            print("🎊 Congratulations! You completed the game!")
            break
        else:
            retry = input("😢 You didn’t win this time. Try again? (yes/no): ").strip().lower()
            if retry != "yes":
                print("Thanks for playing! 👋")
                break

if __name__ == "__main__":
    main()