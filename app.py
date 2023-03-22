from logic import Player, ComputerPlayer, Choice

choices = [
    Choice("Rock", defeats=["Scissors"]),
    Choice("Paper", defeats=["Rock"]),
    Choice("Scissors", defeats=["Paper"]),
]

print("*******************************")
print("Rock, Paper, Scissors 3000 (TM)")
print("*******************************")
player1 = Player("Player")
player2 = ComputerPlayer()
keep_playing = True
round = 0

while keep_playing:
    round += 1
    print("\n")
    print(f"Round {round}")
    print("\n")

    choice1 = player1.choose(choices=choices)
    choice2 = player2.choose(choices=choices)
    print(f"Player chooses: {choice1}")
    print(f"Computer chooses: {choice2}")

    if choice1 == choice2:
        print("Tie!")
    elif choice1.wins_against(choice2):
        print(f"{choice1} beats {choice2} - {player1.name} wins!")
        player1.increase_score()
    else:
        print(f"{choice2} beats {choice1} - {player2.name} wins!")
        keep_playing = False

    print(f"Current score: {player1} vs. {player2}")
    if keep_playing:
        input("Press Enter to start a new round")
        print("Starting a new round...")

    print(f"{player2.name} wins the game!")
    print("Thanks for playing!")
