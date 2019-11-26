 # Turn Based Battle Simulator

# Player and computer take turns to attack each other with different moves
# until one is defeated.

import random


def main():
    """Main function that will welcome the player to the game."""

    print("\tWelcome to Battle Sim! This is a turn based combat simulator where")
    print("\tthere can only be one winner.")

    print("\nHow to play.\n\nPlayers take turn to choose a move. Moves can either deal moderate damage")
    print("with a low range, deal high damage but over a wide")
    print("range, or they can heal. (Note: Moves can miss, including Heal!)")

    print("\nEach player starts with 100 health, and the first")
    print("player to reduce their opponent to 0 is the winner.")

    print("\nThat's it! Good luck")

    play_again = True

    # Set up the play again loop
    while play_again:
        winner = None
        player_health = 100
        computer_health = 100

        # determine whose turn it is
        turn = random.randint(1, 2)  # heads or tails
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("\nPlayer will go first.")
        else:
            player_turn = False
            computer_turn = True
            print("\nComputer will go first.")

        print("\nPlayer health: ", player_health, "Computer health: ", computer_health)

        # set up the main game loop
        while (player_health != 0 or computer_health != 0):

            heal_up = False  # determine if heal has been used by the player. Resets false each loop.
            miss = False  # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected
            moves = {"Punch": random.randint(18, 25),
                     "Mega Punch": random.randint(10, 35),
                     "Heal": random.randint(20, 25)}

            if player_turn:
                print("\nPlease select a move:\n1. Punch (Deal damage between 18-25)\n2. Mega Punch (Deal damage between 10-35)\n3. Heal (Restore between 20-25 health)\n")

                player_move = input("> ").lower()

                move_miss = random.randint(1, 5)  # 20% of missing
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0  # player misses and deals no damage
                    print("You missed!")
                else:
                    if player_move in ("1", "punch"):
                        player_move = moves["Punch"]
                        print("\nYou used Punch. It dealt ", player_move, " damage.")
                    elif player_move in ("2", "mega punch"):
                        player_move = moves["Mega Punch"]
                        print("\nYou used Mega Punch. It dealt ", player_move, " damage.")
                    elif player_move in ("3", "heal"):
                        heal_up = True  # heal activated
                        player_move = moves["Heal"]
                        print("\nYou used Heal. It healed for ", player_move, " health.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else:  # computer turn

                move_miss = random.randint(1, 5)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0  # the computer misses and deals no damage
                    print("The computer missed!")
                else:
                    if computer_health > 30: 
                        if player_health > 75:
                            computer_move = moves["Punch"]
                            print("\nThe computer used Punch. It dealt ", computer_move, " damage.")
                        elif player_health > 35 and player_health <= 75:  # computer decides whether to go big or play it safe
                            imoves = ["Punch", "Mega Punch"]
                            imoves = random.choice(imoves)
                            computer_move = moves[imoves]
                            print("\nThe computer used ", imoves, ". It dealt ", computer_move, " damage.")
                        elif player_health <= 35:
                            computer_move = moves["Mega Punch"]  # FINISH HIM!
                            print("\nThe computer used Mega Punch. It dealt ", computer_move, " damage.")                       
                    else:  # if the computer has less than 30 health, there is a 50% chance they will heal
                        heal_or_fight = random.randint(1, 2) 
                        if heal_or_fight == 1:
                            heal_up = True
                            computer_move = moves["Heal"]
                            print("\nThe computer used Heal. It healed for ", computer_move, " health.")
                        else:
                            if player_health > 75:
                                computer_move = moves["Punch"]
                                print("\nThe computer used Punch. It dealt ", computer_move, " damage.")
                            elif player_health > 35 and player_health <= 75:
                                imoves = ["Punch", "Mega Punch"]
                                imoves = random.choice(imoves)
                                computer_move = moves[imoves]
                                print("\nThe computer used ", imoves, ". It dealt ", computer_move, " damage.")
                            elif player_health <= 35:
                                computer_move = moves["Mega Punch"]  # FINISH HIM!
                                print("\nThe computer used Mega Punch. It dealt ", computer_move, " damage.")

            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > 100:
                        player_health = 100  # cap max health at 100. No over healing!
                else:
                    computer_health += computer_move
                    if computer_health > 100:
                        computer_health = 100
            else:
                if player_turn:
                    computer_health -= player_move
                    if computer_health < 0:
                        computer_health = 0  # cap minimum health at 0
                        winner = "Player"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 0
                        winner = "Computer"
                        break

            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)

            # switch turns
            player_turn = not player_turn
            computer_turn = not computer_turn

        # once main game while loop breaks, determine winner and congratulate

        if winner == "Player":
            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)
            print("\nCongratulations! You have won. You're an animal!!")
        else:
            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)
            print("\nSorry, but your opponent wiped the floor with you. Better luck next time.")

        print("\nWould you like to play again?")

        answer = input("> ").lower()
        if answer not in ("yes", "y"):
            play_again = False


main()